"""
This module contains the views for the church app.
"""

from django.shortcuts import render
from django.conf import settings
from django.contrib import messages

from address.models import Address
from person.forms import PersonForm
from person.models import Person


def about(request):
    """
    This view returns the about page of the church.
    
    :param request: The HTTP request object.
    :return: The rendered about page.
    """
    return render(request, "church/about.html", {})

def home(request):
    return render(request, "church/home.html", {})

def church(request):
    """
    This view returns the church page of the church.
    """
    all_persons = Person.objects.all()
    return render(request, "church/church.html", {
        "all_persons": all_persons,
        })

def contact(request):
    """
    This view returns the contact page of the church.
    """
    return render(request, "church/contact.html", {})
