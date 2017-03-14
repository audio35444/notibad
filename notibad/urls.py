from django.conf.urls import include,url
from . import views

urlpatterns = [
     url(r'^$',views.notibad_list),
     url(r'^noticia/(?P<pk>[0-9]+)/$', views.noticia_detail),
]