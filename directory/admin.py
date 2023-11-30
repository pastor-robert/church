from django.contrib import admin
from address.models import AddressField
from address.forms import AddressWidget
from .models import Church
#from person.admin import PersonInline

class MembershipInline(admin.TabularInline):
    model = Church.crowds.through
    fk_name = 'church'

@admin.register(Church)
class ChurchAdmin(admin.ModelAdmin):
    inlines= (MembershipInline,)
    exclude = ('crowds',)
    model = Church

    formfield_overrides = {
            AddressField: {
                "widget": AddressWidget(
                    attrs={
                        "style": "width: 300px;"})}}