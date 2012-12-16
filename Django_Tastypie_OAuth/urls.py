from django.conf.urls import patterns, include, url

from tastypie.api import Api
from django.contrib import admin
from employee.resources import UserResource, EmployeeResource
admin.autodiscover()


v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(EmployeeResource())

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(v1_api.urls)),
)
