from django.test import TestCase, Client
from django.contrib.auth.models import User
from address.models import Address
from .models import Person
from .admin import PersonAdmin

class PersonAdminTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = User.objects.create_superuser('admin', 'admin@test.com', 'password')
        self.client.force_login(self.admin_user)
        self.address = Address.objects.create(
            # Add the necessary fields for the address
        )
        self.person = Person.objects.create(
            name='Test Person',
            address=self.address
        )

    def test_person_listed(self):
        response = self.client.get('/admin/person/person/')
        self.assertContains(response, 'Test Person')

    def test_person_change_page(self):
        url = f'/admin/person/person/{self.person.id}/change/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)