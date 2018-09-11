from django.conf.urls import url
from . import views

#localhost/errorshooting/...
urlpatterns = [
    url(r'^$', views.index,name='index'),
]