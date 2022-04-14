# imports
import sys

import pandas as pd
import sqlalchemy

import functions
import numpy as np

#########################################################
ds_engine = functions.connect_to_sql()

#########################################################
# loading excel to dataframe
tables = ['AV_BASE_TXN_01_01',
'AV_BASE_TXN_01_02',
'AV_BASE_TXN_02_01',
'AV_BASE_TXN_02_02',
'AV_BASE_TXN_03_01',
'AV_BASE_TXN_03_02',
'AV_BASE_TXN_04_01',
'AV_BASE_TXN_04_02']
for table in tables:
    print('Processing table {}'.format(table))
    path = './data_import/{}.xlsx'.format(table)
    df = functions.data_processing.load_excel_to_df(path)
    # ds_engine.execute('TRUNCATE TABLE {}'.format(table))
    df.to_sql('AV_BASE_TXN', con=ds_engine, if_exists='append', index=False, index_label='SUPERSUBJECT_NK',
              dtype={'SUPERSUBJECT_NK': sqlalchemy.VARCHAR(45)})

