# -*- coding: utf-8 -*-
from rest_framework import routers
from django.urls import include, path

from .views import BitcoinMarketViewSet, BCMViewSet

router = routers.DefaultRouter()
router.register('bitcoin', BitcoinMarketViewSet, basename='db_mode') # ModelViewSet
# Issue: APIView好像不能這樣register, not working
# router.register('bitcoin-json', BCMViewSet, basename='json_mode')    # APIView

urlpatterns = [
    path('', include(router.urls)),
    path('bitcoin-json', BCMViewSet.as_view()), # cuz Issue in line 9
]