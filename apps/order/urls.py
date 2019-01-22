from django.conf.urls import url
from django.contrib import admin

from apps.order import views

urlpatterns = [
    url('^cartadd/', views.cart_add)
]
