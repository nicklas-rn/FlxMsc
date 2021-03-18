import json
from .models import *
from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


def cookieCart(request):
    # Create empty cart for now for non-logged in user
    try:
        cart = json.loads(request.COOKIES['cart'])

    except:
        cart = {}
        print('CART:', cart)

    items = []
    order = {'get_cart_total': 0, 'get_cart_items': 0}
    cartItems = order['get_cart_items']

    for i in cart:
        # We use try block to prevent items in cart that may have been removed from causing error
        try:
            cartItems += cart[i]['quantity']
            print(f"Reading cookie for Beat with id {i}")
            title = cart[i]['license'].replace("_", " ")

            beat = Beat.objects.get(id=i)
            print(beat.title)

            license = get_license_object(beat, title)

            print(f"Selected license: {title}")
            print(license.title)

            total = license.price

            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]['quantity']

            item = {
                'id': beat.id,
                'product': {'id': beat.id, 'title': beat.title, 'license': license.title, 'price': license.price,
                            'imageURL': beat.thumbnail}, 'quantity': cart[i]['quantity'], }
            items.append(item)

        except:
            pass

    print(order['get_cart_total'])

    return {'cartItems': cartItems, 'order': order, 'items': items}


def cookieTransactionId(request):
    try:
        transaction_id_cookie = json.loads(request.COOKIES['transactionIdCookie'])
        print("transactionId worked")
        transaction_id = transaction_id_cookie['transactionId']
        print("Cookie Util view:", transaction_id)

    except:
        print("transactionId didn't work")
        transaction_id = ""

    return transaction_id


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def get_license_object(beat, license_name):
    if license_name == "Basic License":
        license = beat.basiclicense_set.get(title=license_name)

    if license_name == "Premium License":
        license = beat.premiumlicense_set.get(title=license_name)

    if license_name == "Premium Plus License":
        license = beat.premiumpluslicense_set.get(title=license_name)

    if license_name == "Unlimited License":
        license = beat.unlimitedlicense_set.get(title=license_name)

    if license_name == "Exclusive License":
        license = beat.exclusivelicense_set.get(title=license_name)

    return license


