from django.urls import path, include
from rest_framework.routers import DefaultRouter

from retail.views import ChainViewSet
from retail.apps import RetailConfig

app_name = RetailConfig.name
router = DefaultRouter()


router.register(r"api/chain/", ChainViewSet, basename="chain")

urlpatterns = [
                  path('', include(router.urls)),
              ]
