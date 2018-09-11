from django.conf.urls import url
from . import views

#localhost/script/...
urlpatterns = [
    url(r'^$', views.index,name='index'),  
]