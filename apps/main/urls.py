from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^main$', views.mainindex),
    url(r'^read/(?P<id>\d+)$', views.read),
    url(r'^create/(?P<id>\d+)$', views.create),
    url(r'^update/(?P<id>\d+)$', views.update),
    url(r'^delete/(?P<id>\d+)$', views.delete),
]