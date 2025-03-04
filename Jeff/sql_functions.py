# We import a method from the  modules to address environment variables and 
# we use that method in a function that will return the variables we need from .env 
# to a dictionary we call sql_config

from dotenv import dotenv_values

def get_sql_config():
    '''
        Function loads credentials from .env file and
        returns a dictionary containing the data needed for sqlalchemy.create_engine()
    '''
    needed_keys = ['host', 'port', 'database','user','password']
    dotenv_dict = dotenv_values(".env")
    sql_config = {key:dotenv_dict[key] for key in needed_keys if key in dotenv_dict}
    return sql_config

# Import sqlalchemy and pandas - do this only when instructed

import sqlalchemy 

import pandas as pd

# Insert the get_data() function definition below - do this only when instructed in the notebook

def get_data(x):
    '''Connect to the PostgreSQL database server, run query and return data'''

    # get the connection configuration using the get_sql_config function
    sql_config = get_sql_config()
    # create a connection engine to the PostgreSQL server
    engine = sqlalchemy.create_engine('postgresql://user:pass@host/database',
                    connect_args=sql_config # dictionary with config details
                    )
    
    # open a conn session using with, run the query, and return the results
    with engine.begin() as conn: 
        results = conn.execute(x)
        return results.fetchall()

# Insert the get_dataframe() function definition below - do this only when instructed in the notebook

# define a new function get_dataframe() based on format of get_data() but using read_sql_query()
def get_dataframe(x):
    '''Connect to the PostgreSQL database server, run query and return data'''

    # get the connection configuration using the get_sql_config function
    sql_config = get_sql_config()
    # create a connection engine to the PostgreSQL server
    engine = sqlalchemy.create_engine('postgresql://user:pass@host/database',
                    connect_args=sql_config # dictionary with config details
                    )
    return(pd.read_sql_query(x, con=engine))


# Insert the get_engine() function definition below - when instructed

def get_engine():
    sql_config = get_sql_config()
    engine = sqlalchemy.create_engine('postgresql://user:pass@host/database',
                        connect_args=sql_config
                        )
    return engine        

