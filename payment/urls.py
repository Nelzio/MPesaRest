from django.urls import path
from . import views


urlpatterns = [
    path('c2b/', views.c2b_api, name="url_c2b"),
    path('b2c/', views.b2c_api, name="url_b2c"),
]
