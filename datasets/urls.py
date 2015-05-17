from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.DatasetListView.as_view(), name='dataset-list'),
    url(r'^new/', views.DatasetCreateView.as_view(), name='dataset-new'),
    url(r'^(?P<id>[0-9]+)/', views.DatasetDetailView.as_view(), name='dataset-detail'),    
]