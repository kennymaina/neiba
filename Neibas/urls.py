from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    url(r'^$',views.home, name='home'),
    url(r'^profile/$',views.profile,name='profile'),
    # url(r'^new_hood/', views.hood, name='hood'), 
    url(r'^upload/', views.upload_hood, name='upload'),
    url(r'^hoods/',views.hoodie,name='hood'),
    url(r'^search/', views.search, name='search'),
    url(r'^upload_business/', views.upload_business, name='upload_business'),


]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)