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
tables = ['ZMENA_CG_01_01',
'ZMENA_CG_01_02',
'ZMENA_CG_02_01',
'ZMENA_CG_02_02',
'ZMENA_CG_03_01',
'ZMENA_CG_03_02',
'ZMENA_CG_04_01',
'ZMENA_CG_04_02']
for table in tables:
    print('Processing table {}'.format(table))
    path = './data_import/{}.xlsx'.format(table)
    df = functions.data_processing.load_excel_to_df(path)
    df['D_ORIG'] = pd.to_datetime(df['D_ORIG']).dt.date
    # ds_engine.execute('TRUNCATE TABLE {}'.format(table))
    df.to_sql('ZMENA_CG_ORIG', con=ds_engine, if_exists='append', index=False, index_label='SUPERSUBJECT_NK',
              dtype={'SUPERSUBJECT_NK': sqlalchemy.VARCHAR(45)})

