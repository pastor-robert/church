from django.db import models
from address.models import Address, AddressField

class Person(models.Model):
    name = models.CharField(max_length=200)
    address = AddressField(related_name='+', blank=True, null=True)
    church = models.ForeignKey('Church', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.address})"

class Church(models.Model):
    name = models.CharField(max_length=200)
    address = AddressField(related_name='+', blank=True, null=True)


    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=200)
    people = models.ManyToManyField(Person, related_name='groups', through='GroupMember')

    def __str__(self):
        return self.name
    
class GroupMember(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    role = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.person} ({self.group})"