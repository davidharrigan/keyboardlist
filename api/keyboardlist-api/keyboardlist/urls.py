from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers

from .views import IndexView
from keyboards.views import KeyboardViewSet, ManufacturerViewSet
from sellers.views import SellerViewSet, KeyboardInventoryViewSet

router = routers.DefaultRouter()
router.register(r'keyboards', KeyboardViewSet, 'keyboards')
router.register(r'manufacturers', ManufacturerViewSet, 'manufacturers')
router.register(r'sellers', SellerViewSet, 'sellers')
router.register(r'inventories', KeyboardInventoryViewSet, 'inventories')


urlpatterns = [
    url(r'^ingestion/', include('ingestion.urls', namespace='ingestion')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls, namespace="api")),
    url(r'^.*$', IndexView.as_view(), name='index'),
]
