#!/usr/bin/env python
# coding: utf-8

# # Notebook para agregar 100 arquivos parquet do arquivo ZIP '06120089' em um único parquet para pré processamento

# ## Importação bibliotecas

# In[ ]:


get_ipython().system('pip install pyarrow')
get_ipython().system('pip install fastparquet')
get_ipython().system('pip install pandas')
get_ipython().system('pip install numpy')
get_ipython().system('pip install seaborn')
get_ipython().system('pip install matplotlib')
get_ipython().system('pip install scikit-learn')
get_ipython().system('pip install scipy.stats')
get_ipython().system('pip install dask dask[dataframe]')
get_ipython().system('pip install tslearn')
get_ipython().system('pip install tensorflow')
get_ipython().system('pip install pocketbase')


# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pyarrow.parquet as pq
from sklearn.preprocessing import RobustScaler
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SelectFromModel
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
import scipy.stats as stats
import os
import dask.dataframe as dd
from pocketbase import Client


# ## Carregamento dos arquivos parquet, seleção das colunas desejadas e concantenação dos arquivos

# In[ ]:


def concatenate_and_count_rows_in_parquet_files(file_path, filtered_cols):
    total_rows = 0
    list_of_dfs = []  # Lista para armazenar os DataFrames lidos

    # Lista de arquivos Parquet no diretório especificado
    # parquet_files = [file for file in os.listdir(file_path) if file.endswith('.parquet')]

    client = Client('http://0.0.0.0:8090')

    # Remember to create an admin user before running this code
    # Also remember to create a collection named 'parquets' before running this code
    # And fill it with at least one document

    admin_data = client.admins.auth_with_password('test@test.com', '1234567890')
    result = client.collection('parquets').get_list(1, 20, {})

    for item in result.items:
        id = str(item).split(' ')[1].split('>')[0]
        obj = client.collection('parquets').get_one(id=id)
        url = "http://0.0.0.0:8090/api/files/parquets/" + id + "/" + obj.parquet
        df = pd.read_parquet(url, engine='pyarrow')
        total_rows += len(df)
        list_of_dfs.append(df)
        print(f"Arquivo {obj.parquet} tem {len(df)} linhas.")
    
    # # Loop para ler cada arquivo Parquet, contar as linhas e armazenar o DataFrame na lista
    # for file_name in parquet_files:
    #     full_path = os.path.join(file_path, file_name)
    #     df = dd.read_parquet(full_path, columns=filtered_cols)
    #     total_rows += len(df)
    #     list_of_dfs.append(df)
    #     print(f"Arquivo {file_name} tem {len(df)} linhas.")
    
    # Concatenar todos os Dask DataFrames em um único Dask DataFrame
    concatenated_df = dd.concat(list_of_dfs, interleave_partitions=True)
    
    return concatenated_df, total_rows

# Uso da função
file_path = "primeiro_arquivo_zip/"
filtered_cols = ['recording_time', 'dateDay-1', 'dateMonth-1', 'dateYear-1', 'phaseOfFlight-1',
                  'message0418DAA-1','message0422DAA-1','amscHprsovDrivF-1a', 'amscHprsovDrivF-1b',
                  'amscHprsovDrivF-2b', 'amscPrsovDrivF-1a',
                  'amscPrsovDrivF-1b', 'amscPrsovDrivF-2b',
                  'basBleedLowPressF-1a', 'basBleedLowPressF-2b',
                  'basBleedLowTempF-1a', 'basBleedLowTempF-2b',
                  'basBleedOverPressF-1a', 'basBleedOverPressF-2b',
                  'basBleedOverTempF-1a', 'basBleedOverTempF-2b',
                  'bleedFavTmCmd-1a', 'bleedFavTmCmd-1b',
                  'bleedFavTmCmd-2a', 'bleedFavTmCmd-2b', 'bleedFavTmFbk-1a',
                  'bleedFavTmFbk-1b', 'bleedFavTmFbk-2b', 'bleedHprsovCmdStatus-1a',
                  'bleedHprsovCmdStatus-1b', 'bleedHprsovCmdStatus-2a',
                  'bleedHprsovCmdStatus-2b', 'bleedHprsovOpPosStatus-1a',
                  'bleedHprsovOpPosStatus-1b', 'bleedHprsovOpPosStatus-2a',
                  'bleedHprsovOpPosStatus-2b', 'bleedMonPress-1a',
                  'bleedMonPress-1b', 'bleedMonPress-2a', 'bleedMonPress-2b',
                  'bleedOnStatus-1a', 'bleedOnStatus-1b', 'bleedOnStatus-2b',
                  'bleedOverpressCas-2a', 'bleedOverpressCas-2b',
                  'bleedPrecoolDiffPress-1a', 'bleedPrecoolDiffPress-1b',
                  'bleedPrecoolDiffPress-2a', 'bleedPrecoolDiffPress-2b',
                  'bleedPrsovClPosStatus-1a', 'bleedPrsovClPosStatus-2a',
                  'bleedPrsovFbk-1a']

resulting_df, total_rows = concatenate_and_count_rows_in_parquet_files(' ', filtered_cols)
print(f"O número total de linhas em todos os arquivos é: {total_rows}")


# In[ ]:


resulting_df.info()


# In[ ]:


resulting_df.describe()


# ## Remoção de linhas duplicadas com base todas as colunas exceto a 'record_time' 

# In[6]:


def remove_duplicates_except_record_time(dask_df):
    """
    Remove linhas duplicadas com base em todas as colunas, exceto 'record_time'.

    Parâmetros:
    - dask_df: DataFrame Dask de entrada.

    Retorna:
    - DataFrame Dask com linhas duplicadas removidas.
    """
    
    # Crie uma lista de colunas a serem consideradas ao identificar duplicatas
    columns_to_consider = [col for col in dask_df.columns if col != 'record_time']
    
    # Use o método drop_duplicates do Dask para remover duplicatas com base nas colunas especificadas
    #Mantém o primeiro valor duplicado por default
    unique_df = dask_df.drop_duplicates(subset=columns_to_consider)
    
    return unique_df

# Uso da função
unique_df = remove_duplicates_except_record_time(resulting_df)


# In[ ]:


# Contar o número de linhas em 'unique_df' (depois da remoção de duplicatas)
after_row_count = len(unique_df)

# Imprimir os resultado
print(f"Número de linhas depois da remoção de duplicatas: {after_row_count}")


# ## Remoção de valores NaN das colunas de data

# In[8]:


data_df = unique_df

columns_to_fill = ['dateYear-1', 'dateMonth-1', 'dateDay-1']
data_df[columns_to_fill] = data_df[columns_to_fill].fillna(0)


# ## Criação da coluna 'data_voo' e exclusão das colunas de ano,mês e dia

# In[ ]:


import pandas as pd

def create_data_voo(row):
    year = int(row['dateYear-1'])
    month = int(row['dateMonth-1'])
    day = int(row['dateDay-1'])

    # Verificar se a data é válida
    if 1 <= month <= 12 and 1 <= day <= 31:
        return f"{year}-{str(month).zfill(2)}-{str(day).zfill(2)}"
    else:
        return pd.NaT  # Retorna "Not a Timestamp" para datas inválidas

# Assuming data_df is your DataFrame
data_df['data_voo'] = data_df.apply(create_data_voo, axis=1)
data_df['data_voo'] = pd.to_datetime(data_df['data_voo'], errors='coerce')

print(data_df)


# In[ ]:


# Verificar valores inválidos em 'dateMonth-1'
invalid_months = data_df[data_df['dateMonth-1'].isin(list(range(13, 100)) + [0])]['dateMonth-1']
print("Invalid months:", invalid_months)

# Verificar NaNs nas colunas de data
nan_counts_before = data_df[['dateYear-1', 'dateMonth-1', 'dateDay-1']].isna().sum()
print("\nNaN counts before transformation:")
print(nan_counts_before)


# In[11]:


import pandas as pd

# Assuming you've already defined data_df and performed the necessary transformations

# Create a new column 'data_voo'
data_df['data_voo'] = data_df.apply(create_data_voo, axis=1)
data_df['data_voo'] = pd.to_datetime(data_df['data_voo'], errors='coerce')

# Drop unwanted columns
data_voo_df = data_df.drop(columns=['dateDay-1', 'dateMonth-1', 'dateYear-1'])

# Reorder columns
cols = data_voo_df.columns.tolist()
cols.insert(1, cols.pop(cols.index('data_voo')))
data_voo_df = data_voo_df[cols]

# Now you can proceed with using data_voo_df
new_data_voo_df = data_voo_df.copy()


# In[ ]:


new_data_voo_df.head()


# # Gravação dos dados do DataFrame feito em Dask em novo arquivo parquet

# In[13]:


new_data_voo_df.to_parquet('new_data_voo.parquet')


# In[ ]:


from sqlalchemy import create_engine

# con = pyodbc.connect('postgresql://postgres:yourpassword@localhost:5432/postgres')
database_url = 'postgresql://postgresql:yourpassword@localhost:5432/postgres'
engine = create_engine(database_url)
mario_de_andrade = new_data_voo_df.head()
mario_de_andrade.to_sql("Data", engine)

