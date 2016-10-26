from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^logreg$', views.logreg_page),
    url(r'^sports$', views.sports_page),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout)
]
