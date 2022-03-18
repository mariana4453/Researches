# imports
import pandas as pd
import functions
import numpy as np

#########################################################


#########################################################
# loading excel to dataframe
tables = ['NPS_klienti']
for table in tables:
    print('Processing table {}'.format(table))
    path = './data/{}.xlsx'.format(table)

    df = functions.datastore_processing.load_excel_to_df(path)

    ds_engine.execute('TRUNCATE TABLE {}'.format(table))
    df.to_sql(table, con=ds_engine, if_exists='replace', index=False, index_label='SUPERSUBJECT_NK')


