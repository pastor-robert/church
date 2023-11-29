from django.conf import settings
from django.shortcuts import render
from address.models import Address
from person.forms import PersonForm
from person.models import Person, Church

# Create your views here.

def home(request):
    addresses = Address.objects.all()
    success = False
    google_api_key_set = bool(settings.GOOGLE_API_KEY)
    person_set = Person.objects.all()

    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            success = True
            form.save()
    else:
        form = PersonForm(initial={"address": Address.objects.last()})

    context = {
            "form": form,
            "google_api_key_set": google_api_key_set,
            "success": success,
            "addresses": addresses,
            "person_set": person_set,
            }
    return render(request, "person/home.html", context)

def about(request):
    return render(request, "person/about.html", {})
def contact(request):
    return render(request, "person/about.html", {})
def log_message(request):
    return render(request, "person/about.html", {})

def church(request):
    all_persons = Person.objects.all()
    return render(request, "person/church.html", {
        "all_persons": all_persons,
        })