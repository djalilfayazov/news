from django.urls import *
from .views import index


urlpatterns = [

    path('', index, name='index')

]