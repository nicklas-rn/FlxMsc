from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('beats/<keyword>/', views.beats, name='beats'),
    path('beats/beat-detail/<title>/', views.beat_detail, name='beat_detail'),
    path('cart/', views.cart, name='cart'),
    path('summary/', views.summary, name='summary'),
    path('process_order/', views.process_order, name='process_order'),
    path('create_license_pdf/', views.generate_obj_pdf, name='create_license'),
    path('mybeats/', views.mybeats, name='mybeats'),
    path('transactionIdGuide/', views.transactionId_guide, name='transactionId_guide'),
    path('contact/', views.contact, name='contact'),
    path('dsgvo/', views.dsgvo, name='dsgvo'),
]