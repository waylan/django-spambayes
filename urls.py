from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^django_spambayes/', include('django_spambayes.foo.urls')),

    # Uncomment this for admin:
    (r'^admin/(.*)', admin.site.root),
    (r'^sb_demo/', include('sb_demo.urls')),
    (r'^comments/', include('django.contrib.comments.urls')),
)
