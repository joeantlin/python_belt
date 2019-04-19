from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^dashboard$', views.mainindex),
    url(r'^read/(?P<id>\d+)$', views.read),
    url(r'^trips/new$', views.pagecreate),
    url(r'^trips/edit/(?P<id>\d+)$', views.editpage),
    url(r'^create/(?P<id>\d+)$', views.create),
    url(r'^update/(?P<id>\d+)$', views.update),
    url(r'^join/(?P<id>\d+)$', views.join),
    url(r'^delete/(?P<id>\d+)/(?P<tripid>\d+)$', views.delete),
]