from django.conf.urls import *

from core import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'report$', views.generate_graph, name='report'),
]
