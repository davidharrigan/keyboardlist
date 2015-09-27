from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^ingestion/', include('ingestion.urls', namespace='ingestion')),
    url(r'^keyboards/', include('keyboards.urls', namespace='keyboards')),
    url(r'^sellers/', include('sellers.urls', namespace='sellers')),
    url(r'^admin/', include(admin.site.urls)),
)
