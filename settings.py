import csv

import pandas as pd
import data_save as ds
set_file_name = 'settings.csv'

def load_file_settings(setting_file):
    file = pd.read_csv(setting_file)
    return file


def load_settings(row, setting_file):
    #  by name? or by row?

    temp_df = load_file_settings(setting_file)
    data = temp_df.loc[row, 'Data']
    setting_name = temp_df.loc[row, 'setting name']
    int_value = temp_df.loc[row, 'int_value']
    boolean_value = temp_df.loc[row, 'boolean']
    str_value = temp_df.loc[row, 'str_value']
    return data, setting_name, int_value, boolean_value, str_value


def save_settings(df, filename):
    df.to_csv(filename, index=False)


def add_settings(setting_file, df, list_of_settings):
    """ taking list of settings len(4), with paramets: name, int, boolean, str"""

    row = len(df) + 1
    df.loc[row, 'Data'] = int(row)
    df.loc[row, 'setting name'] = list_of_settings[0]
    df.loc[row, 'int_value'] = list_of_settings[1]
    df.loc[row, 'boolean'] = list_of_settings[2]
    df.loc[row, 'str_value'] = list_of_settings[3]

    save_settings(df, setting_file)

def change_setting(set_file_name, df, row, setting_to_change, value_to_change):
    if row <= len(df):
        df.loc[row, setting_to_change] = value_to_change

        # save settings here
        save_settings(df, set_file_name)

        return df
    else:
        print('to high value')




#Test Area

# df = load_file_settings(set_file_name)
# g = change_setting(set_file_name,df, 0, 'boolean', True)



# backup csv
# setting name,int_value,boolean,str_value
# testowy,20,True,Dir
