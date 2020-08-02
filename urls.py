
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="Home"),
    path('create_url', views.createUrl, name="CreateUrl"),
    path('<str:code>', views.openUrl, name="OpenUrl"),
]
