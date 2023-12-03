from django import forms
from address.forms import AddressField, AddressWidget
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        address = AddressField()
        fields = [
            'name', 'address',
            'email', 'phone_number',
        ]
        widgets= {'address': AddressWidget(attrs={"style":"width: 300px"})}