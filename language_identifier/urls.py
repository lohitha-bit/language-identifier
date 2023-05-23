from django.urls import path
from identifier.views import index

urlpatterns = [
         path('', index, name='index'),
     ]