from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('yes/', views.yes_page, name='yes'),
    path('no/', views.no_page, name='no'),
]
