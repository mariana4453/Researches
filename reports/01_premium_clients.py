import json
import sys

import sqlalchemy

import functions
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

#########################################################################
ds_engine = functions.datastore_functions.connect_to_sql()

#########################################################################
def save_df_to_excel(dataframe, path, sheet_name):
    functions.log_info('Exporting dataframe to excel...\n')
    with pd.ExcelWriter(path, date_format='DD-MM-YYYY') as writer:
        dataframe.to_excel(writer, sheet_name=sheet_name, index=False, index_label='SUPERSUBJECT_NK')

path = "./data_import/12_CG_ZMENA.xlsx"

query = "SELECT * FROM researches.NPS_CG_ZMENA;"
df = functions.datastore_query(ds_engine, query)

save_df_to_excel(df, path, "CG_ZMENA")

