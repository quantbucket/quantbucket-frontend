from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
 	url(r'^algorithms/', include('algorithms.urls', namespace="algorithms")),
  	url(r'^datasets/', include('datasets.urls', namespace="datasets")),
  	url(r'^analysis/', include('analysis.urls', namespace="analysis")), 	  	
    url(r'^admin/', include(admin.site.urls)),
]