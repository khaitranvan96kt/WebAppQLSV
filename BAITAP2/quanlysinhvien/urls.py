from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    url(r'^$', views.index),
    url(r'^register/', views.register),
    url(r'^showlist/', views.showlist),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)