# -*- coding: utf-8 -*-
from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import BitcoinMarket


class BitcoinMarketSerializer(serializers.ModelSerializer):
    """
    model mode
    """
    datetime   = serializers.DateField()
    time_high  = serializers.DateTimeField()
    time_low   = serializers.DateTimeField()
    open_price = serializers.DecimalField(max_digits=30, decimal_places=15)
    high_price = serializers.DecimalField(max_digits=30, decimal_places=15)
    low_price  = serializers.DecimalField(max_digits=30, decimal_places=15)
    close_price= serializers.DecimalField(max_digits=30, decimal_places=15)
    volume     = serializers.DecimalField(max_digits=30, decimal_places=15)
    market_cap = serializers.DecimalField(max_digits=30, decimal_places=15)


    class Meta:
        model = BitcoinMarket
        fields = '__all__'


class BCMSerializer(serializers.Serializer):
    """
    without model: read data.csv
    """
    datetime   = serializers.CharField()
    time_high  = serializers.DateTimeField()
    time_low   = serializers.DateTimeField()
    open_price = serializers.DecimalField(max_digits=30, decimal_places=15)
    high_price = serializers.DecimalField(max_digits=30, decimal_places=15)
    low_price  = serializers.DecimalField(max_digits=30, decimal_places=15)
    close_price= serializers.DecimalField(max_digits=30, decimal_places=15)
    volume     = serializers.DecimalField(max_digits=30, decimal_places=15)
    market_cap = serializers.DecimalField(max_digits=30, decimal_places=15)
