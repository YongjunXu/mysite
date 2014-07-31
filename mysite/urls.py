from django.conf.urls import include, url
from django.contrib import admin
from mysite.views import *
from books.views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('^time/$', current_datetime),
    url('^meta/$',display_meta),
    # url('^search-form/$',search_form),
    url('^search/$',search),
    url('^contact/$',contact),
    url('^test/$',testform),#the first form
    url('^test/test-next/$',testnext_form),#the second form
]
