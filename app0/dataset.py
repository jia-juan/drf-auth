# -*- coding: utf-8 -*-



class BitcoinMarket:
    def __init__(self, datetime, time_high, time_low, open_price, high_price, low_price, close_price, volume, market_cap):
        self.datetime = datetime
        self.time_high = time_high
        self.time_low = time_low
        self.open_price = open_price
        