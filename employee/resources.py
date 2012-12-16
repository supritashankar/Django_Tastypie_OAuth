from django.contrib.auth.models import User
from tastypie.resources import ModelResource
from employee.models import Employee
from tastypie.authentication import OAuthAuthentication

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'

class EmployeeResource(ModelResource):
    class Meta:
        queryset = Employee.objects.all()
        resource_name = 'employee'
        authentication = OAuthAuthentication()

