from django.contrib import admin
from django.urls import path, include
from app import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.input),
    path('inputprocess/', views.input_process),
    path('items/', views.list_items)
]

urlpatterns += staticfiles_urlpatterns()