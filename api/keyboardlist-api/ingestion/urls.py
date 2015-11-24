from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.DataIngestionView.as_view(), name='ingest')
]
