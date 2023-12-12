'''
admin.py is a file that allows you to register your models with the Django admin application.
'''

from django.contrib import admin
from address.models import AddressField
from address.forms import AddressWidget
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from .models import Crowd


class MemberInline(admin.TabularInline):
    """ Member Admin Inline """
    model = Crowd.persons.through

@admin.register(Crowd)
class CrowdAdmin(admin.ModelAdmin):
    """Crowd Admin """
    inlines = [MemberInline]
    exclude = ('persons',)
