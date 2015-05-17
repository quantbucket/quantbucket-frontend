from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.AlgorithmListView.as_view(), name='algorithm-list'),
    url(r'^new/', views.AlgorithmCreateView.as_view(), name='algorithm-new'),
    url(r'^(?P<id>[0-9]+)/', views.AlgorithmDetailView.as_view(), name='algorithm-detail'),    
]