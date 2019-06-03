from django.conf.urls import url,include
from . import views
from django.conf import settings
from .views import *


urlpatterns = [
    url(r'^$',views.home, name='home'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^new_hood/', views.hood, name='hood'),
]
