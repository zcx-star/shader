from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static
 
urlpatterns = [
    url(r'^$', views.index),  
    url(r'^admin/', admin.site.urls),
    url(r'^shader/', include('shader.urls')),          
    url(r'^errorshooting/', include('errorshooting.urls')), 
    url(r'^script/', include('script.urls')),         
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)