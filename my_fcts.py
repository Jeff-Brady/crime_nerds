# # # # # # # # # # # # # # # # # # # #
#                                     #
#          Unify column names         #
#                                     #
# # # # # # # # # # # # # # # # # # # #

def format_columns(df):
    df.columns = (df.columns
                .str.lower()
                .str.strip()
                .str.replace(' ', '_')
                .str.replace('-', '_')
                .str.replace('/', '_'))

# # # # # # # # # # # # # # # # # # # #
#                                     #
#        Notification script          #
#                                     #
# # # # # # # # # # # # # # # # # # # #

import os
import subprocess

def play_sound_and_notify():
        for n in range(3):
            os.system('afplay /System/Library/Sounds/Hero.aiff')

        apple_script = f'display dialog "Task done!" buttons {{"OK"}}'
        subprocess.run(['osascript', '-e', apple_script])


# # # # # # # # # # # # # # # # # # # #
#                                     #
#   Concatenate 2 or more csv files   #
#                                     #
# # # # # # # # # # # # # # # # # # # #

import pandas as pd

def csv_concat():
    # You will be asked to enter the number of csv files
    nr_of_csv = int(input('No. of files to concatenate? '))
    df_list = []
    for i in range(1,nr_of_csv + 1):
        # You will be asked to enter the path of each csv file you want to concatenate
        filepath = input(f"Enter file path of {i} csv file")
        # Data frame of each csv will be created and pushed to the list
        df = pd.read_csv(filepath)
        df_list.append(df)
    # Here is where the data frames will be concatenated 
    concat_df = pd.concat(df_list, ignore_index=True)
    # Naming the file. No '.csv' needed.
    concat_df.to_csv(f'{input("Enter file name")}.csv', index=False)
    # 1st way of notification, if the function was successful
    # print(f'Data was concatenated!')
    # 2nd way of notification, if the function was successful
    apple_script = f'display dialog "Task done!" buttons {{"OK"}}'
    subprocess.run(['osascript', '-e', apple_script])


# # # # # # # # # # # # # # # # # # # #
#                                     #
# Create a data frame for every sheet #
#                                     #
# # # # # # # # # # # # # # # # # # # #

def excel_to_df():
    # Read excel file and create dict object, containing all sheets
    filepath = input(f"Enter file path of excel file")
    sheet_names = pd.read_excel(filepath, sheet_name=None)
    for name in sheet_names:
        # For every sheet in the workbook, create a new data frame
        exec(f"{name}_df = pd.DataFrame(sheet_names[name])")
        # Show the name of the sheet and its data frame created
        print(f"Created '{name}_df' from '{name}' sheet.")


# # # # # # # # # # # # # # # # # # # #
#                                     #
#        Check for NaN values         #
#                                     #
# # # # # # # # # # # # # # # # # # # #

def check_nan(df):
    null_columns = df.isnull().any()
    null_count = df.isnull().sum()
    for column, has_null in null_columns.items():
        if has_null:
            print(f"'{column}' has {null_count[column]} missing values.\nTo drop the rows use:\n'YOUR_DF.dropna(subset=['{column}'], inplace=True)'\n")
            #drop_null = df.dropna(subset=[column], inplace=True)
    return


# # # # # # # # # # # # # # # # # # # # # # #
#                                           #
#       SQL DB connection  with .env        #
#                                           #
# # # # # # # # # # # # # # # # # # # # # # #

from dotenv import dotenv_values

def connect_sql_db():

    '''
        Function loads credentials from .env file and
        returns a dictionary containing the data needed for sqlalchemy.create_engine()
    '''
    needed_keys = ['app_token', 'usr', 'pw']

    dotenv_dict = dotenv_values(".env")

    sql_config = {key:dotenv_dict[key] for key in needed_keys if key in dotenv_dict}

    return sql_config


# # # # # # # # # # # # # # # # # # # # # # #
#                                           #
#      Retrieve data from PostgreSQL        #
#                                           #
# # # # # # # # # # # # # # # # # # # # # # #

import sqlalchemy

def get_data(sql_query):

    '''Connect to the PostgreSQL database server, run query and return data'''

    # get the connection configuration using the connect_sql_db function
    sql_config = connect_sql_db()

    # create a connection engine to the PostgreSQL server
    engine = sqlalchemy.create_engine('postgresql://user:password@host/database',
                    connect_args=sql_config # dictionary with config details
                    )
    
    # open a conn session using with, run the query, and return the results
    with engine.begin() as conn: 
        results = conn.execute(sql_query)
        return results.fetchall()


# # # # # # # # # # # # # # # # # # # # # # #
#                                           #
#  Connect to SQL DB and return data frame  #
#                                           #
# # # # # # # # # # # # # # # # # # # # # # #

def get_dataframe(sql_query):

    ''' 
    Connect to the PostgreSQL database server, 
    run query and return data as a pandas dataframe
    '''

    # get the connection configuration using the connect_sql_db function
    sql_config = connect_sql_db()

    # create a connection engine to the PostgreSQL server
    engine = sqlalchemy.create_engine('postgresql://user:password@host/database',
                    connect_args=sql_config # dictionary with config details
                    )
    
    # open a conn session using with, run the query, and return the results
    return pd.read_sql_query(sql=sql_query, con=engine)


# # # # # # # # # # # # # # # # # # # # # # #
#                                           #
#        PostgreSQL engine creation         #
#                                           #
# # # # # # # # # # # # # # # # # # # # # # #

def get_engine():
    sql_config = connect_sql_db()
    engine = sqlalchemy.create_engine('postgresql://user:password@host/database',
                        connect_args=sql_config
                        )
    return engine     

