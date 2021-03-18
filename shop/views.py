from django.shortcuts import render, redirect, reverse, HttpResponse
from .models import Beat, BasicLicense, PremiumLicense, PremiumPlusLicense, UnlimitedLicense, ExclusiveLicense, Order, OrderItem, PageLink, ContactRequest
from .utils import cookieCart, cookieTransactionId, render_to_pdf, get_license_object
from .forms import ContactForm
import json
from django.views import View
from django.core.files import File
from io import BytesIO
import time, datetime


def home(request):
    data = cookieCart(request)
    cartItems = data['cartItems']

    beats = Beat.objects.all().order_by('-id')[:5]
    page_links = PageLink.objects.all().order_by('-id')[:4]

    context = {
        'beats': beats,
        'cartItems': cartItems,
        'page_links': page_links,
    }

    return render(request, 'shop/home.html', context)


def beats(request, keyword):
    data = cookieCart(request)
    cartItems = data['cartItems']

    if keyword == "nokeyword":
       beats = Beat.objects.all()
    else:
        beats = Beat.objects.filter(keywords__contains=keyword)
    context = {
        'beats': beats,
        'cartItems': cartItems
    }
    return render(request, 'shop/beats.html', context)


def beat_detail(request, title):
    data = cookieCart(request)
    cartItems = data['cartItems']

    title = title.replace("_", " ")
    beat = Beat.objects.get(title=title)
    basic_license = beat.basiclicense_set.get(beat__title=title)
    premium_license = beat.premiumlicense_set.get(beat__title=title)
    license_list = []
    license_list.append(basic_license)
    license_list.append(premium_license)
    try:
        premiumplus_license = beat.premiumpluslicense_set.get(beat__title=title)
        license_list.append(premiumplus_license)
    except PremiumPlusLicense.DoesNotExist:
        pass
    try:
        unlimited_license = beat.unlimitedlicense_set.get(beat__title=title)
        license_list.append(unlimited_license)
    except UnlimitedLicense.DoesNotExist:
        pass
    try:
        exclusive_license = beat.exclusivelicense_set.get(beat__title=title)
        license_list.append(exclusive_license)
    except ExclusiveLicense.DoesNotExist:
        pass

    context = {
        'beat': beat,
        'license_list': license_list,
        'cartItems': cartItems
    }
    return render(request, 'shop/beat_detail.html', context)


def cart(request):
    data = cookieCart(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items,
               'order': order,
               'cartItems': cartItems
               }
    print(items)

    return render(request, 'shop/cart.html', context)


def summary(request):
    data = cookieCart(request)
    cartItems = data['cartItems']

    transactionId = cookieTransactionId(request)
    order = Order.objects.get(transaction_id=transactionId)
    order_items = order.orderitem_set.all()
    print("Summary View: ", order.transaction_id, order.customer, order.orderitem_set.all())

    print("Summary view:", order.customer)

    context = {
        'order': order,
        'order_items': order_items,
        'cartItems': cartItems,
    }

    return render(request, 'shop/summary.html', context)


def process_order(request):
    data = json.loads(request.body)
    cart_data = cookieCart(request)

    print('(VIEW) body:', data['payerFirstName'], data['payerLastName'])

    order, created = Order.objects.get_or_create(transaction_id=data['transactionId'])
    order.transaction_id = data['transactionId']
    order.customer = f"{data['payerFirstName']} {data['payerLastName']}"
    order.save()

    for item in cart_data['items']:
        order_item = OrderItem.objects.create()
        order_item.order = order
        order_item.beat = Beat.objects.get(title=item['product']['title'])
        order_item.license = item['product']['license']
        order_item.save()

        print("Process Order View: ", order_item.beat)
        print("Process Order View: ", order_item.order)

    print("Process Order View: ", order.transaction_id, order.customer, order.orderitem_set.all())

    request.session['processing_order_completed'] = True
    print("Process Order View:  processing completed")

    return render(request, 'shop/cart.html')


def generate_obj_pdf(request):

    # sleep to await order creation completion
    time.sleep(5)

    print('Awaiting order processing completion')
    while True:
        processing_order_completed = request.session.get('processing_order_completed')
        if processing_order_completed is True:
            print('Order processing completed')
            break

        request.session['processing_order_completed'] = False
    transactionId = cookieTransactionId(request)
    while True:
        try:
            order = Order.objects.get(transaction_id=transactionId)
            break
        except:
            order = None
    order_items = order.orderitem_set.all()
    print("Generate PDF View: ", order.transaction_id, order.customer, order.orderitem_set.all())
    print("Generating PDF view:", order_items)

    for order_item in order_items:
        license = get_license_object(order_item.beat, order_item.license)
        date = datetime.date.today()

        data = {
            'order': order,
            'order_item': order_item,
            'license': license,
            'date': date,
        }
        print("Generating PDF for", order_item.license)
        title = order_item.beat.title
        license_pdf = render_to_pdf('shop/license_pdf.html', data)
        pdf_name = "LicensePDF_%s.pdf" %(title)
        order_item.license_pdf.save(pdf_name, File(BytesIO(license_pdf.content)))
        print("Generating PDF view PDF creation:", order_item.license_pdf)

    return redirect('summary')


def mybeats(request):
    data = cookieCart(request)
    cartItems = data['cartItems']

    context = {
        'cartItems': cartItems
    }
    return render(request, 'shop/mybeats.html', context)


def transactionId_guide(request):
    data = cookieCart(request)
    cartItems = data['cartItems']

    context = {
        'cartItems': cartItems
    }
    return render(request, 'shop/transactionId_guide.html', context)


def contact(request):
    data = cookieCart(request)
    cartItems = data['cartItems']

    form = ContactForm

    context = {
        'cartItems': cartItems,
        'form': form,
    }

    if request.method == 'POST':
        form = form(data=request.POST)

        if form.is_valid():
            contact_request = ContactRequest.objects.create()

            contact_subject = request.POST.get(
                'contact_subject'
                , '')
            contact_email = request.POST.get(
                'contact_email'
                , '')
            contact_content = request.POST.get('contact_content', '')

            contact_request.email_address = contact_email
            contact_request.subject = contact_subject
            contact_request.content = contact_content
            contact_request.save()
        return redirect('contact')

    return render(request, 'shop/contact.html', context)


def dsgvo(request):
    data = cookieCart(request)
    cartItems = data['cartItems']
    context = {
        'cartItems': cartItems,
    }
    return render(request, 'shop/dsgvo.html', context)

