from django import forms
from address.forms import AddressField, AddressWidget
from .models import Church

class ChurchForm:
    class Meta:
        model = Church
        address = AddressField()
        fields = "__all__,people"
        widgets= {'address': AddressWidget(attrs={"style":"width: 300px"})}
