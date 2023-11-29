from django import forms
from address.forms import AddressField, AddressWidget
from .models import Person, Church

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        address = AddressField()
        fields = "__all__"
        widgets= {'address': AddressWidget(attrs={"style":"width: 300px"})}

class ChurchForm:
    class Meta:
        model = Church
        address = AddressField()
        fields = "__all__,people"
        widgets= {'address': AddressWidget(attrs={"style":"width: 300px"})}