from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^sendmail/$', views.sendmail(), name='sendemail'),
                       )
