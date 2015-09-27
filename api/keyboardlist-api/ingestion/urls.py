from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.DataIngestionView.as_view(), name='ingest')
)
