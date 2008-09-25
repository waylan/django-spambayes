from django.conf.urls.defaults import *


urlpatterns = patterns('',
    (r'^add/?', 'sb_demo.views.add_comment'),
    (r'^train/?', 'sb_demo.views.train'),
    (r'.*', 'sb_demo.views.index'),
)
