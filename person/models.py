"""Person model."""

from django.db import models
from address.models import AddressField
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class Contact(models.Model):
    name = models.CharField(max_length=200)
    address = AddressField(related_name='+', null=True, blank=True)

class Person(Contact):
    """Person model.
    """
    email = models.EmailField(blank=True)
    email_confirmed = models.BooleanField(default=False)
    #password_hash = models.CharField(max_length=128)
    #security_stamp = models.CharField(max_length=128)
    #concurrency_stamp = models.CharField(blank=True, max_length=128)
    phone_number = PhoneNumberField(
        region="US",
        blank=True,
    )
    phone_number_confirmed = models.BooleanField(default=False)
    #two_factor_enabled = models.BooleanField(default=False)
    #lockout_end = models.DateTimeField(null=True)
    #lockout_enabled = models.BooleanField(default=False)
    #access_failed_count = models.IntegerField(default=0)


    def __str__(self):
        return f"{self.name} / {self.address or self.email or self.phone_number.as_national}"

class Crowd(Contact):
    """A group of people."""
    persons = models.ManyToManyField(Person, related_name='crowds')


    def __str__(self):
        return f"{self.name}"
