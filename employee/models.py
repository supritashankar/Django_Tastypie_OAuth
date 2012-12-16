
from django.db import models

# Create your models here.

class Person(models.Model):
    """ every employee is mapped to a person """
    email = models.CharField(max_length=30, unique=True, db_index=True)
    name = models.CharField(max_length=70)
    number = models.CharField(max_length=15)

    def __unicode__(self):
        return self.email


class Employee(models.Model):
    """ The Employee class which defines a unique employee """
    DESIGNATION = (
        (1, 'CEO/Board member'),
        (4, 'Senior Management'),
        (8, 'Middle management'),
        (12, 'Staff'),
    )
    GENDER = ( (u'M', 'Male'), (u'F', 'Female'), (u'N', 'Refuse to identify'), )

    person      = models.ForeignKey(Person, db_index=True)
    empid       = models.CharField(max_length=25)
    dob         = models.DateField(help_text='Date of birth', blank=True, null=True)
    location    = models.CharField(max_length=40, blank=True, null=True)
    hobbies     = models.CharField(max_length=30, blank=True, null=True)
    gender      = models.CharField(max_length=1, choices=GENDER, blank=True, null=True)
    designation = models.PositiveIntegerField(choices=DESIGNATION, blank=True, null=True)

    def __unicode__(self):
        return '{0} employee with employee id {1}'.format(self.person, self.empid)


