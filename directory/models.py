from django.db import models
from address.models import AddressField
from person.models import Crowd

class Church(Crowd):
    """A church is a crowd of people who gather at a specific location"""
    address = AddressField(related_name='+', blank=True, null=True)
    """Oddly, a church also *contains* crowds of people"""
    crowds = models.ManyToManyField(Crowd, related_name='churches')

    def __str__(self):
        return self.name
