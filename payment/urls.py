from django.urls import path
from . import views


urlpatterns = [
    path('purchase/', views.purchase_api),
]
