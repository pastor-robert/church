from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='person.home'),
    path('contact/', views.contact, name='person.contact'),
    path('log/', views.log_message, name='person.log'),
]
