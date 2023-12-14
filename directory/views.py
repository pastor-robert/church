from django.shortcuts import render
from django.contrib import messages
from address.models import Address

from church import settings
from person.models import Person
from person.forms import PersonForm

# Create your views here.

def home(request):
    """
    This view returns the church directory.

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
            messages.success(request, f"Succesfully added {form.cleaned_data['name']} to the database.")
        else: 
            messages.error(request, "Please correct the errors below.") 

    form = PersonForm()

    context = {
            "form": form,
            "google_api_key_set": google_api_key_set,
            "success": success,
            "addresses": addresses,
            "person_set": person_set,
            }
    return render(request, "directory/home.html", context)
