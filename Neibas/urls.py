from django.conf.urls import url,include
from . import views
from django.conf import settings
from .views import *


urlpatterns = [
    url(r'^$',views.home, name='home'),
]
