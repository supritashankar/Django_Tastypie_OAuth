
from django.db import models

# Create your models here.

class Person(models.Model):
    """ every employee is mapped to a person """
    email = models.CharField(max_length=30, unique=True, db_index=True)
    name = models.CharField(max_length=70)
    number = models.CharField(max_length=15)


class Employee(models.Model):
    """ The Employee class which defines a unique employee """
    person = models.ForeignKey(Person, db_index=True)
    empid = models.CharField(max_length=25)


