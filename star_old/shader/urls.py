from django.conf.urls import url
from . import views

#localhost/shader/...
urlpatterns = [
    url(r'^$', views.index,name='index'),   
    url(r'^Roboto/$', views.Roboto,name='Roboto'),                      
    url(r'^Roboto/(?P<shader_name>.*)', views.detail, name='detail'),  
    url(r'^Test/$', views.Test,name='Test'),   
]