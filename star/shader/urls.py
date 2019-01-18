from django.conf.urls import url
from . import views

app_name = 'shader'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^update$', views.update, name='update'),
    url(r'^(?P<shader_name>.*)', views.detail, name='detail'), 
]