
from django.contrib import admin
from django.urls import path, include
import showdatas 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('showdatas.urls')),
]
