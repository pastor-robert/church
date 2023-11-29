from django.contrib import admin
from address.models import AddressField
from address.forms import AddressWidget
from .models import Person, Church, Group

class PersonAdminInline(admin.TabularInline):
    model = Person
    verbose_name = 'aaaa'
    verbose_name_plural = 'bbbb'

class MembershipInline(admin.TabularInline):
    model = Group.people.through
    verbose_name = 'Group'
    verbose_name_plural = 'Group Membership'

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    #list_display = (
    #        'id',
    #        'first_name',
    #        'address',
    #        )
    formfield_overrides = {
            AddressField: {
                "widget": AddressWidget(
                    attrs={
                        "style": "width: 300px;"})}}
    inlines = (MembershipInline,)

@admin.register(Church)
class ChurchAdmin(admin.ModelAdmin):
    inlines= (PersonAdminInline,)
    model = Church

    #list_display = (
    #        'id',
    #        'name',
    #        'address',
    #        )
    formfield_overrides = {
            AddressField: {
                "widget": AddressWidget(
                    attrs={
                        "style": "width: 300px;"})}}

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    inlines = (MembershipInline,)
    exclude = ('people',)