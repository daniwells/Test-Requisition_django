from django.contrib import admin
from django.urls import path
import showdatas 
from . import views

urlpatterns = [
    path('', views.show_datas, name="showdatas"),
    path('get_csrf_token/', views.get_csrf_token, name='get_csrf_token'),
]
