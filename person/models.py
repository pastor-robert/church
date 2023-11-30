"""Person model."""

from django.db import models
from address.models import AddressField

class Person(models.Model):
    """_summary_

    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """
    name = models.CharField(max_length=200)
    address = AddressField(related_name='+', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.address})"

class Crowd(models.Model):
    """A group of people."""
    name = models.CharField(max_length=200)
    persons = models.ManyToManyField(Person, related_name='crowds')

    def __str__(self):
        return f"{self.name}"