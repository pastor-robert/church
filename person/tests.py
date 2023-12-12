"""_summary_ """

from django.test import TestCase
from address.models import Address
from .models import Person

class PersonModelTest(TestCase):
    """Test models.Person model"""
    def setUp(self):
        self.address = Address.objects.create(
            # Add the necessary fields for the address
        )
        self.person = Person.objects.create(
            name='Test Person',
            address=self.address
        )

    def test_person_creation(self):
        self.assertEqual(self.person.name, 'Test Person')
        self.assertEqual(self.person.address, self.address)

    def test_person_str(self):
        self.assertEqual(str(self.person), f'Test Person ({self.address})')
