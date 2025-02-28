from django.urls import path
from . import views

app_name = 'studyapp'

from django.shortcuts import render

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
