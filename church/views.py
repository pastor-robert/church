from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render
from address.models import Address
from person.forms import PersonForm
from person.models import Person

def about(request):
    return render(request, "church/about.html", {})

def home(request):
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
