import sys

import functions
import pandas as pd
import numpy as np

##########################################################
ds_engine = functions.datastore_functions.connect_to_sql()

##########################################################
# importing excel for test
path = "./data_import/Prehlad_2Q_2022_EBA.xlsx"
df = pd.DataFrame(pd.read_excel(path, sheet_name='PREHĽAD'))

# 1 - loc
# case - case sensitive, default True

# df.loc[df['OFFER_NAME'].str.contains('Calling', case=False), 'Calling_offers'] = 'Calling'
# counts = df['Calling_offers'].value_counts(dropna=True)
# functions.datastore_functions.datastore_store(ds_engine, df, 'df_test', 'SUPERSUBJECT_NK')


# 2 - np.select
# patterns = [
#             (df['OFFER_NAME'].str.contains('Calling', case=False, regex=False), 'Calling'),
#             (df['OFFER_NAME'].str.contains('Dialog', case=False, regex=False), 'Dialog')
#             ]
# conditions, values = zip(*patterns)
# df['Offer_type'] = np.select(conditions, values, None)
# df['Offer_type'] = df['Offer_type'].combine_first(df['OFFER_NAME'])
#
# functions.datastore_functions.datastore_store(ds_engine, df, 'df_test', 'SUPERSUBJECT_NK')