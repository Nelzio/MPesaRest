from django.shortcuts import render
from .models import Entradas
from .forms import EntradasModelForm


def home(request):
    data = {}
    cad = Entradas(page="API Payment")  # @classmethod is used here
    cad.save()
    return render(request, 'home/cover.html', data)


def payment(request):
    data = {}
    cad = Entradas(page="API Payment")  # @classmethod is used here
    cad.save()
    return render(request, 'home/payment.html', data)
