from django.urls import path
from main import views
from . import views

urlpatterns = [
    path('',views.index),
]
