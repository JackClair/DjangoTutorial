from django.contrib import admin
from django.urls import path
from django.urls import include
from AppTwo import views
urlpatterns = [
    path('', views.user, name="help")
]
