from django.shortcuts import render
from .models import Entradas


def home(request):
    # data = {}
    # cad = Entradas(page="API Payment")  # @classmethod is used here
    # cad.save()
    return render(request, 'home/cover.html')


def payment(request):
    # data = {}
    # cad = Entradas(page="API Payment")  # @classmethod is used here
    # cad.save()
    return render(request, 'home/payment.html')


def paymentb2c(request):
    return render(request, 'home/paymentb2c.html')
