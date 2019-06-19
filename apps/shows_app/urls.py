from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^validate_name$', views.validate_name),
    url(r'^shows/(?P<num>\d+)/update$', views.update),
    url(r'^shows/(?P<num>\d+)/destroy$', views.destroy),
    url(r'^shows/(?P<num>\d+)/edit$', views.edit),
    url(r'^shows/(?P<num>\d+)$', views.show),
    url(r'^shows/create$', views.create),
    url(r'^shows/new$', views.new),
    url(r'^shows$', views.shows),
    url(r'^', views.index)
]