# -*- coding: utf-8 -*-
import os
import csv
import json
import datetime
import dateutil.parser

import pandas as pd

# from models import BitcoinMarket

def raw_data_parse():
    """
    convert raw_data.json to data.csv
    """
    with open(os.getcwd()+'/app0/raw_data.json', 'r') as fp:
        data = json.loads(fp.read())

    df = pd.DataFrame(data)
    extend_col = list(df.loc[0]['quote']['USD'].keys())
    extend_col.pop()

    for col in extend_col:
        df[col] = df['quote'].apply(lambda x: x['USD'][col])
    
    df.drop(['quote', 'time_open', 'time_close'] ,axis=1,inplace=True)
    df['datetime'] = df['time_high'].apply(lambda x: datetime.datetime.strftime(dateutil.parser.parse(x), '%Y-%m-%d'))
    df = df[['datetime', 'time_high', 'time_low', 'open', 'high', 'low', 'close', 'volume', 'market_cap']]
    df.to_csv(os.getcwd()+'/app0/data.csv')

def csv_to_db():
    with open(os.getcwd()+'/app0/data.csv') as fp:
        reader = csv.reader(fp)
        next(reader, None) # skip headers: https://stackoverflow.com/questions/48716446/python-skip-header-row-with-csv-reader
        for row in reader:
            print(row[9])
            # _, created = BitcoinMarket.objects.create(
                
            # )

if __name__ == "__main__":
    # raw_data_parse()
    # print(BitcoinMarket.objects.all())