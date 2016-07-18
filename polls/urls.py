from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       # url(r'^sendmail/$', views.sendmail(), name='sendemail'),
                       url(r'^check/$', views.check_request, name='check'),
                       url(r'^name/$', views.get_name, name='get_name'),
                       url(r'^add/$', views.add, name='add'),
                       url(r'^add_post/$', views.add_form, name='add'),
                       )
