from django import forms
from address.forms import AddressField, AddressWidget
from phonenumber_field.formfields import PhoneNumberField
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        address = AddressField()
        phone_numbr = PhoneNumberField()
        fields = [
            'name', 'address',
            'email', 'phone_number',
            'portrait'
        ]
        widgets = {
            'address': AddressWidget(),
        }

