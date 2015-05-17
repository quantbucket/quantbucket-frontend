from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.AnalysisListView.as_view(), name='analysis-list'),
    url(r'^new/', views.AnalysisWizard.as_view(), name='analysis-new'),
    url(r'^(?P<id>[0-9]+)/', views.AnalysisDetailView.as_view(), name='analysis-detail'),    
]