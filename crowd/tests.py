"""_summary_ """

from django.test import TestCase
from address.models import Address
from .models import Crowd
from .. import person

class CrowdModelTest(TestCase):
    """Test models.Person model"""
    def setUp(self):
        self.empty_crowd = Crowd.objects.create(
            name='Empty Crowd',
        )
        self.a_crowd = Crowd.objects.create(
            name='A Crowd',
        )
        self.b_crowd = Crowd.objects.create(
            name='B Crowd',
        )
        self.c_crowd = Crowd.objects.create(
            name='C Crowd',
        )
        self.x_person = person.models.Person.objects.create(
            name='X Person',
        )
        self.y_person = person.models.Person.objects.create(
            name='Y Person',
        )
        self.z_person = person.models.Person.objects.create(
            name='Z Person',
        )

        self.a_crowd.persons.add(self.x_person)
        self.b_crowd.persons.add(self.x_person)
        self.b_crowd.persons.add(self.y_person)
        self.c_crowd.persons.add(self.y_person)
        self.c_crowd.persons.add(self.z_person)

    def test_crowd_str(self):
        self.assertEqual(self.empty_crowd.name, 'Empty Crowd')
        self.assertEqual(self.a_crowd.name, 'A Crowd')
        self.assertEqual(self.b_crowd.name, 'B Crowd')
        self.assertEqual(self.c_crowd.name, 'C Crowd')

    def test_crowd_count(self):
        self.assertEqual(self.a_crowd.persons.count(), 1)
        self.assertEqual(self.b_crowd.persons.count(), 2)
        self.assertEqual(self.c_crowd.persons.count(), 2)

    def test_person_count(self):
        self.assertEqual(self.x_person.crowds.count(), 2)
        self.assertEqual(self.y_person.crowds.count(), 2)
        self.assertEqual(self.z_person.crowds.count(), 1)
