"""
This file is used to create the views for the person app.
"""

from django.shortcuts import render
from person.models import Person


def contact(request):
    """
    This view returns the contact page of the church.
    """
    return render(request, "person/about.html", {})

def log_message(request):
    """
    This view returns the log_message page of the church.
    """
    return render(request, "person/about.html", {})

