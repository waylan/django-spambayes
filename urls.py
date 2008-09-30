""" Sample urls.py for the demo app. """

from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/(.*)', admin.site.root),
    (r'^sb_demo/', include('sb_demo.urls')),
    (r'^comments/', include('django.contrib.comments.urls')),
)
