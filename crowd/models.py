"""Person model."""

from django.db import models
from address.models import AddressField
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
import person

class Crowd(person.models.Contact):
    """A group of people."""
    persons = models.ManyToManyField(person.models.Person, related_name='crowds')

    def __str__(self):
        return f"{self.name}"
