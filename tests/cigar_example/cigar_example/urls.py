from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('cigar_example.restapi.urls', namespace="cigars")),
    url(r'^', include('rest_framework_swagger.urls', namespace='swagger')),
]
