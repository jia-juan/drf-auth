# -*- coding: utf-8 -*-
from django.db import models


class BitcoinMarket(models.Model):
    datetime   = models.DateField()
    time_high  = models.DateTimeField()
    time_low   = models.DateTimeField()
    open_price = models.DecimalField(max_digits=30, decimal_places=15)
    high_price = models.DecimalField(max_digits=30, decimal_places=15)
    low_price  = models.DecimalField(max_digits=30, decimal_places=15)
    close_price= models.DecimalField(max_digits=30, decimal_places=15)
    volume     = models.DecimalField(max_digits=30, decimal_places=15)
    market_cap = models.DecimalField(max_digits=30, decimal_places=15)
    