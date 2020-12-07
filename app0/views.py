# -*- coding: utf-8 -*-
import os
import json

import pandas as pd
from django.shortcuts import render
from rest_framework import views
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.decorators import action
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import BitcoinMarket
from .serializers import BitcoinMarketSerializer  # model mode
from .serializers import BCMSerializer            # without model
# from .simpleviewset import SimpleViewSet
from .permissions import HighFlexibilityPermission
from .permissions import GroupPermission


class BitcoinMarketViewSet(viewsets.ModelViewSet):
    """
    Issue: ModelViewSet queryset 支援without model嗎？
    驗證: 覆寫get_queryset()
    """
    # queryset = BitcoinMarket.objects.all()
    serializer_class = BCMSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    """
    Issue: 同一ModelViewSet內不同action的permission mapping, 於get_permissions進行mapping
    參考: https://stackoverflow.com/questions/35970970/django-rest-framework-permission-classes-of-viewset-method
    """
    # authentication_classes = (JSONWebTokenAuthentication, )  # settings.py已經做過全域設定, 這邊可以不用叻
    permission_classes_by_action = {'get_history': [HighFlexibilityPermission, ],
                                    'get_by_datetime': [GroupPermission, ]}

    # FIXME: 覆寫get_queryset()後, self.queryset仍為None
    def get_queryset(self):
        data = pd.read_csv(os.getcwd() + '/app0/data.csv', index_col=0).to_json(orient='records')

        return json.loads(data)

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]

    @action(detail=False, methods=['get'])
    def get_history(self, request, **kwargs):
        queryset = self.get_queryset()  # Issue: 這樣每次都會load一次資料, 如何讓self.get_queryset()初始執行?
        serializer = BCMSerializer(data=queryset, many=True)
        """
        Issue: AssertionError: When a serializer is passed a `<keyword>` keyword argument you must call `.is_valid()` before attempting to access the serialized `.data` representation.
        """
        try:
            serializer.is_valid()
        except Exception:
            raise RuntimeError('serializer is not valid, cuz: %s' % serializer.errors)
        return Response(serializer.data)

    @action(detail=False,
            methods=['get'],
            url_path='get_by_datetime/(?P<datetime>[^/.]+)')  # Memo: 使用url_path傳遞參數
    def get_by_datetime(self, request, datetime, **kwargs):
        queryset = self.get_queryset()
        query = next((dict0 for dict0 in queryset if dict0['datetime'] == datetime), None)  # 參考: https://stackoverflow.com/questions/8653516/python-list-of-dictionaries-search
        if query is not None:
            serializer = BCMSerializer(data=query)
            try:
                serializer.is_valid()
            except Exception:
                raise RuntimeError('serializer is not valid, cuz: %s' % serializer.errors)

            return Response(serializer.data)
        else:
            return Response({'error': 'can\'t find datetime: %s' % datetime})


class BCMViewSet(views.APIView):

    renderer_classes = [JSONRenderer]
    permission_classes = [permissions.AllowAny]
    swagger_schema = None

    # Issue: AttributeError: type object 'BCMViewSet' has no attribute 'get_extra_actions'
    # https://stackoverflow.com/questions/49721089/django-viewset-has-not-attribute-get-extra-actions
    @classmethod
    def get_extra_actions(cls):
        return []

    def get(self, request, format=None):
        data = pd.read_csv(os.getcwd()+'/app0/data.csv', index_col=0).to_json(orient='records')
        serializer = BCMSerializer(data=json.loads(data), many=True)
        # Issue: AssertionError: When a serializer is passed a `data` keyword argument you must call `.is_valid()` before attempting to access the serialized `.data` representation.
        try:
            serializer.is_valid()
        except Exception:
            raise RuntimeError('serializer is not valid, cuz: %s' % serializer.errors)
        return Response(serializer.data)


@api_view(['get'])
@permission_classes([permissions.AllowAny])
def get_bcmarket(request, format=None, **kwargs):
    pass