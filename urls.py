from django.conf.urls.defaults import patterns, include, url
from MentorMatchApp.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MentorMatch.views.home', name='home'),
    # url(r'^MentorMatch/', include('MentorMatch.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^match/$', match),
    
    #Login, logout, signup
    (r'^logout/$', logoutUser),
    (r'^login/$', loginUser),
    (r'^signup/$', signup),
    
    #Profiles
    (r'^profile/edit/$', user_edit),
    (r'^profile/$', profile),
    (r'^users/search/$', user_search),
    (r'^users/(?P<alias>\w+)/$', display_user),
    (r'^users/$', users),
    
    (r'^add_mentor/(?P<alias>\w+)/$', add_mentor),
    
    (r'^users/$', users),

    (r'^$', home),
)
