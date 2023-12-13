"""
This module contains the views for the church app.
"""

from django.shortcuts import render
from django.conf import settings
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
    """
    This view returns the home page of the church. It also handles the POST request
    for the PersonForm. If the form is valid, it saves the form and sets success to True.
    
    :param request: The HTTP request object.
    :return: The rendered home page.
    """
    addresses = Address.objects.all()
    success = False
    google_api_key_set = bool(settings.GOOGLE_API_KEY)
    person_set = Person.objects.all()

    if request.method == "POST":
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            success = True
            form.save()

    form = PersonForm()

    context = {
            "form": form,
            "google_api_key_set": google_api_key_set,
            "success": success,
            "addresses": addresses,
            "person_set": person_set,
            }
    return render(request, "church/home.html", context)

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
