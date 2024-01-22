from django.urls import path

from dollar_api import views

urlpatterns = [
    path('', views.dollar_list_all),
]