from django.conf.urls import patterns, include, url

from registration.backends.default.views import RegistrationView

from sitters.forms import UserTypeRegistrationForm

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'sitters.views.home', name='home'),
    # url(r'^petluvers/', include('petluvers.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^djadmin/', include(admin.site.urls)),

    url(r'accounts/register/$',
        RegistrationView.as_view(form_class=UserTypeRegistrationForm),
        name='registration_register'),

    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^usertype/', 'sitters.views.home', name='home'),
    
    url(r'^(?P<username>[a-zA-Za_zA_Z0-9.-]*)/$', 'sitters.views.profile', name='profile'),
)
