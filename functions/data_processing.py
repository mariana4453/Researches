# imports
import pandas as pd

import sys
import functions

#########################################################################
# loading excel to dataframe
def load_excel_to_df(path):
    functions.log_info('Loading xls to data_import frame ... \n')
    try:
        source = pd.DataFrame(pd.read_excel(path))
    except:
        functions.log_error('Loading xls to data_import frame ... failed. - %s\n')
        sys.exit(1)
    finally:
        functions.log_info('Loading xls to data_import frame ... done.\n')
        return source