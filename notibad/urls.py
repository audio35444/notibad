from django.conf.urls import include,url
from . import views

urlpatterns = [
     url(r'^$',views.notibad_list),
     url(r'^noticia/(?P<pk>[0-9]+)/$', views.noticia_detail),
     url(r'^noticia/new/$', views.noticia_new, name='noticia_new'),
     url(r'^noticia/(?P<pk>[0-9]+)/edit/$', views.noticia_edit, name='noticia_edit'),
     url(r'^noticia/(?P<pk>\d+)/remove/$', views.noticia_remove, name='noticia_remove'),
]