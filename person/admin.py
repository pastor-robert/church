'''
admin.py is a file that allows you to register your models with the Django admin application.
'''

from django.contrib import admin
from address.models import AddressField
from address.forms import AddressWidget
from .models import Person, Crowd


#class PersonInline(admin.TabularInline):
#    """ Person Admin Inline """
#    model = Person

#class CrowdInline(admin.TabularInline):
#    """ Crowd Admin Inline """
#    model = Crowd

class MemberInline(admin.TabularInline):
    """ Member Admin Inline """
    model = Crowd.persons.through

@admin.register(Crowd)
class CrowdAdmin(admin.ModelAdmin):
    """Crowd Admin """
    inlines = [MemberInline]
    exclude = ('persons',)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    """Person Admin """
    formfield_overrides = {
            AddressField: {
                "widget": AddressWidget(
                    attrs={
                        "style": "width: 300px;"})}}
    inlines = [MemberInline]
