from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='url_home'),
    path('docs/c2b', views.payment, name='url_pay_c2b'),
    path('docs/b2c', views.paymentb2c, name='url_pay_b2c'),
]
