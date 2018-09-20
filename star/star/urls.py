from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
	url(r'^$', views.index),  
	url(r'^admin/', admin.site.urls),
    url(r'^shader/', include('shader.urls')),    
] 
urlpatterns += staticfiles_urlpatterns()