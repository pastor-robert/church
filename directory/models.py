from django.db import models
from address.models import AddressField
from person.models import Crowd

class Church(Crowd):
    """
    Church Model
      N.b. The church is-a Crowd, and also has-a Crowd.
    """
    address = AddressField(related_name='+', blank=True, null=True)
    crowds = models.ManyToManyField(Crowd, related_name='churches')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = 'churches'