from django.conf.urls import patterns, include, url

from tastypie.api import Api
from django.contrib import admin
from employee.resources import UserResource, EmployeeResource
admin.autodiscover()


v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(EmployeeResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Django_Tastypie_OAuth.views.home', name='home'),
    # url(r'^Django_Tastypie_OAuth/', include('Django_Tastypie_OAuth.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(v1_api.urls)),
)
