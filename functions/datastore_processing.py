import json
import sys
import pymysql
import pandas as pd
import functions

from cryptography.fernet import Fernet
from sqlalchemy import create_engine


def connect_to_sql():
    # loading config file
    config_path = "./notes/config.json"
    with open(config_path, 'r') as c:
        config = json.load(c)

        f = Fernet(config["secret_key"])
        functions.log_info('Preparing local datastore connection ... \n')
        db = 'mysql+pymysql://{user}:{pw}@{host}/{db}'.format(user=config['mysql_local']['user'], pw=f.decrypt(config["mysql_local"]["password"].encode()).decode(),
                                                              host=config['mysql_local']['host'], db=config['mysql_local']['database'])
        try:
            engine = create_engine(db)
        except:
            functions.log_error('Preparing local datastore connection ... ... failed. - %s\n' % sys.exc_info()[0])
            sys.exit(1)
        finally:
            functions.log_info('Preparing local datastore connection ... done.\n')
            return engine


def datastore_query(ds_engine, query):
    functions.log_info('Datastore query ... \n')
    try:
        df = pd.read_sql_query(query, ds_engine)
    except:
        # tod add log
        functions.log_error('Datastore query ... failed. - %s\n' % sys.exc_info()[0])
        sys.exit(1)
    finally:
        functions.log_info('Datastore query ... done.\n')
        return df


def datastore_store(ds_engine, df_source, df_source_name, index_label):
    functions.log_info('Storing dataframe %s to datastore ... \n' % df_source_name)
    try:
        df_source.to_sql(df_source_name, con=ds_engine, if_exists='replace', index=False, index_label=index_label)
    except:
        functions.log_error('Storing dataframe %s to datastore ... failed. - %s\n' % df_source_name, sys.exc_info()[0])
        sys.exit(1)
    finally:
        functions.log_info('Storing dataframe %s to datastore ... done.\n' % df_source_name)
        return 0



