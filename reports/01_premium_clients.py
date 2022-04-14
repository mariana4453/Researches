import json
import sys
import functions
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#########################################################################
ds_engine = functions.datastore_functions.connect_to_sql()

#########################################################################
def save_df_to_excel(dataframe, path, sheet_name):
    functions.log_info('Exporting dataframe to excel...\n')
    with pd.ExcelWriter(path, date_format='DD-MM-YYYY') as writer:
        dataframe.to_excel(writer, sheet_name=sheet_name, index=False, index_label='SUPERSUBJECT_NK')

path = "./data_import/ORIG_PRODUKTY.xlsx"

query = "SELECT * FROM researches.NPS_ALL_PRODUCTS"
df = functions.datastore_query(ds_engine, query)

save_df_to_excel(df, path, "ORIG_PRODUKTY")

# query = "SELECT * FROM researches.NPS_AV_BASE_TXN;"
# df = functions.datastore_functions.datastore_query(ds_engine, query)
# print(df.columns)
# quantities = df['AVG_CNT_TXN_CARD']
# first = np.quantile(quantities, [0.25, 0.5, 0.75])
# print(first)
# # all_txn 0 , 1-2, 3-5, 6-10, 11-20, 20-30, 30 and more...
# plt.hist(quantities, bins=20)
# plt.show()