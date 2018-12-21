from django.shortcuts import render


def home(request):
    data = {}
    return render(request, 'home/cover.html', data)


def payment(request):
    data = {}
    return render(request, 'home/payment.html', data)
