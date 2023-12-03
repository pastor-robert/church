"""Person model."""

from django.db import models
from address.models import AddressField
from phonenumber_field.modelfields import PhoneNumberField

class Person(models.Model):
    """_summary_

    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """
    name = models.CharField(max_length=200)
    address = AddressField(related_name='+', null=True, blank=True)
    email = models.EmailField(blank=True)
    email_confirmed = models.BooleanField(default=False)
    #password_hash = models.CharField(max_length=128)
    #security_stamp = models.CharField(max_length=128)
    #concurrency_stamp = models.CharField(blank=True, max_length=128)
    phone_number = PhoneNumberField(blank=True)
    phone_number_confirmed = models.BooleanField(default=False)
    #two_factor_enabled = models.BooleanField(default=False)
    #lockout_end = models.DateTimeField(null=True)
    #lockout_enabled = models.BooleanField(default=False)
    #access_failed_count = models.IntegerField(default=0)


    def __str__(self):
        return f"{self.name} ({self.address or self.email or self.phone_number})"

class Crowd(models.Model):
    """A group of people."""
    name = models.CharField(max_length=200)
    persons = models.ManyToManyField(Person, related_name='crowds')

    def __str__(self):
        return f"{self.name}"
