from django.urls import path

from dollar_api import views

urlpatterns = [
    path('', views.api_home, name='home')
]