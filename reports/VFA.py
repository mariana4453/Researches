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
# loading 1st VFA part
# path = "./data_import/Ipsos_Tatra banka Finančný menežmen domácností_dáta.xlsx"
# # load until Q1_1
# df = pd.read_excel(path, sheet_name='data_lab', usecols=range(0, 21), skiprows=2)
# df = pd.DataFrame(df)
# df.to_sql('VFA_1', con=ds_engine, if_exists='replace', index=False, index_label='ID')

query = """SELECT * FROM researches.VFA_1
            WHERE XC3_vek <= 30"""
vfa = functions.datastore_functions.datastore_query(ds_engine, query)

# kolko ludi zije v domacnosti
vfa_byvanie = pd.crosstab(vfa['R4_rodinny_stav'], vfa['XC3_vek'])

sns.heatmap(vfa_byvanie, cmap="YlGnBu", annot=True, cbar=False)
plt.show()


# fig, ax = plt.subplots()
# sns.set_style("poster")
# sns.heatmap(vfa_byvanie, annot=True)
# ax.set_xticklabels(["vlastnim", "nevlastnim"])
# plt.xticks(rotation=30)
# plt.show()




# vfa_crosstab = pd.crosstab(vfa['XC3_vek'], [vfa['R2_zije_v_domacnosti'], vfa['R3_zije_v_domacnosti_do_18']], rownames=["Vek do 30"], colnames=["Kolko zije v domacnosti",
# #                                                                                                                                         "V domacnosti do 18"])
# print(vfa_crosstab)
#
# sns.heatmap(vfa_crosstab, cmap="YlGnBu", annot=True)
# plt.show()




# pd.crosstab([df.make, df.num_doors] - groups in rows, [df.body_style, df.drive_wheels]-
#             groups in columns, rownames=['Auto Manufacturer', "Doors"], colnames=['Body Style', "Drive Type"], dropna=False)
#
# Vizualizing
# sns.heatmap(pd.crosstab([df.make, df.num_doors], [df.body_style, df.drive_wheels]), cmap="YlGnBu", annot=True, cbar=False)


