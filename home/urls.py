from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='url_home'),
    path('pay/', views.payment, name='url_pay'),
]
