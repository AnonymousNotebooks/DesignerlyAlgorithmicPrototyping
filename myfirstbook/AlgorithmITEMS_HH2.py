#!/usr/bin/env python
# coding: utf-8

# ## 4: FUNCTIONS FOR ITEMS PER TIME, STORENAME

# ### Import libraries 

# In[10]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import numpy as np
from random import sample
class bcolors:
    WARNING = '\033[91m'
    BOLD = '\033[1m'


# ### Load and view data 

# In[1]:


# Function to generate #visits per day of the week
from AlgorithmDAYS_HH2 import beforeNY, AfterNY, daysAfterNY
#Function to define the limits for total visits, days, same store and type per week
from AlgorithmCOUNTS_HH2 import CountTotalVisits, CountTotalDays, CountStoreName, CountStoreType, CountTotalPerday, CountVisitsPerDay
# Function to generate #visits per time
from AlgorithmTIMES_HH2 import AlbertHeijn, Okay, Delhaize, Carrefour, VersavelPoelman, Sys, Brabo, Ikea, Kruidvat
# Function to decide amounts per visit & per week
from AlgorithmAMOUNT_HH2 import StoreAmount, WeekAmount, StoreCount, WeekCount, CatCount, PerCatCount, PerCatCountALL, PerCatCountSTORE
# Function to generate store name (&type) per weekday (+ assign #of visits per day)
from AlgorithmSTORE_HH2 import storeperday, countsperstore


# In[4]:


dataframe = pd.read_csv (r"C:\Users\20204113\OneDrive - TU Eindhoven\2_Research\1_Groceries\DATA\9th week - narrative (3rd attempt)\HH2\df\df_HH2.csv")


# # Get counts per store etc

# In[7]:

# df1 = daysAfterNY(dataframe)
# df2 = storeperday(df1)
# df3 = countsperstore(df2)
# df3['I'] = np.arange(df3.shape[0])



# In[31]:

# ADD WEIGHTS PER ITEM TYPE
df = pd.read_csv (r"C:\Users\20204113\OneDrive - TU Eindhoven\2_Research\1_Groceries\DATA\9th week - narrative (3rd attempt)\HH2\df\df_HH2.csv")

df['weights_itemtype'] = df.groupby('item_type')['item_type'].transform('count')

df.to_csv(r"C:\Users\20204113\OneDrive - TU Eindhoven\2_Research\1_Groceries\DATA\9th week - narrative (3rd attempt)\HH2\df\df_HH2.csv", index=False)


# # DEFINE FUNCTIONS

# In[28]:


def supermarket(dataframes, counts, timez):
        ## Create dataframes for each day they go shopping
    typedf = {}
    storetypes = dataframes.store_type.values.tolist()
    times = dataframes.time.values.tolist()           
    thisdaysdf = {}
    daydf = {}
    for storetype in dataframes['store_type']:
            storeday = df[df['store_type'] == storetype]
            items = storeday[['item_type', 'item_name', 'time', 'store_type','store_name', 'amount', 'category', 'weights_itemtype']]
            typedf[storetype] = pd.DataFrame(items)
            typedf[storetype].drop_duplicates()        
    ## Split up the dataframes to store name for mon, tue, sat, sun
    if 'supermarket'in dataframes.values:
            for time in times:
                thisdaydf = typedf['supermarket']
                storesdf = thisdaydf[thisdaydf['time'] == time]
                items = storesdf[['item_type', 'item_name', 'store_type', 'store_name', 'amount', 'category', 'weights_itemtype']]
                daydf[time] = pd.DataFrame(items)
                daydf[time].drop_duplicates()                
    ## Sample the dataframes per day they go shopping
    if 'supermarket' in dataframes.values:
            grocerylist = dataframes[dataframes['store_type'] == 'supermarket']
            if 'supermarket' in dataframes.values:
                daydf[timez]= daydf[timez].drop_duplicates()
                return daydf[timez].sample(n=counts, replace=False)


# In[35]:


def butcher(dataframes, counts):
        ## Create dataframes for each day they go shopping
    typedf = {}
    for storetype in dataframes['store_type']:
            storeday = df[df['store_type'] == storetype]
            items = storeday[['item_type', 'item_name', 'store_type','store_name', 'amount', 'category', 'weights_itemtype']]
            typedf[storetype] = pd.DataFrame(items)
            typedf[storetype].drop_duplicates() 
        ## sample dataframes per store type
    if 'butcher' in dataframes.values:
            grocerylist = dataframes[dataframes['store_type'] == 'butcher']
            if 'butcher' in dataframes.values:
                typedf['butcher'] = typedf['butcher'].drop_duplicates()
                return typedf['butcher'].sample(n=counts, replace=False)


# In[41]:


def bakery(dataframes, counts):
        ## Create dataframes for each day they go shopping
    typedf = {}
    for storetype in dataframes['store_type']:
            storeday = df[df['store_type'] == storetype]
            items = storeday[['item_type', 'item_name', 'store_type','store_name', 'amount', 'category', 'weights_itemtype']]
            typedf[storetype] = pd.DataFrame(items)
            typedf[storetype].drop_duplicates() 
    if 'bakery' in dataframes.values:
        grocerylist = dataframes[dataframes['store_type'] == 'bakery']
        if 'bakery' in dataframes.values:
            typedf['bakery'] = typedf['bakery'].drop_duplicates()
            return typedf['bakery'].sample(n=counts, replace=False)


# In[46]:


def drugstore(dataframes, counts):
        ## Create dataframes for each day they go shopping
    typedf = {}
    for storetype in dataframes['store_type']:
            storeday = df[df['store_type'] == storetype]
            items = storeday[['item_type', 'item_name', 'store_type','store_name', 'amount', 'category', 'weights_itemtype']]
            typedf[storetype] = pd.DataFrame(items)
            typedf[storetype].drop_duplicates() 
    if 'drugstore' in dataframes.values:
            grocerylist = dataframes[dataframes['store_type'] == 'drugstore']
            if 'drugstore' in dataframes.values:
                typedf['drugstore'] = typedf['drugstore'].drop_duplicates()
                return typedf['drugstore'].sample(n=counts, replace=False)


# In[52]:


def furniturestore(dataframes, counts):
        ## Create dataframes for each day they go shopping
    typedf = {}
    for storetype in dataframes['store_type']:
            storeday = df[df['store_type'] == storetype]
            items = storeday[['item_type', 'item_name', 'store_type','store_name', 'amount', 'category', 'weights_itemtype']]
            typedf[storetype] = pd.DataFrame(items)
            typedf[storetype].drop_duplicates() 
    if 'furniture store' in dataframes.values:
            grocerylist = dataframes[dataframes['store_type'] == 'furniture store']
            if 'furniture store' in dataframes.values:
                daydf['furniture store'] = daydf['furniture store'].drop_duplicates()
                return daydf['furniture store'].sample(n=counts, replace=False)
            
            
            
#####
### Check the counts for each ITEM TYPE PER STORE TYPE

# for entire period
def PerTYPECountSTORE(itemtype, storetype):
    df_type = df[df['store_type'] == storetype]
    count = int(df_type['order_ID'].nunique())
    data = {'order_ID': range(count)}
    orderID = pd.DataFrame(data)
    df_type = df_type[df_type['item_type'] == itemtype]
    df_type = df_type.groupby(['order_ID'])['amount'].count()
    df_type = pd.DataFrame (df_type)
    df_type = df_type.reset_index() 
    df_type = orderID.merge(df_type, how='left').fillna(0)
    min = df_type.min(axis=0)['amount']
    max = df_type.max(axis=0)['amount']
    return (min, max)



#####

### Create lists per store type

def supermarkets(dataframes, index):
    storesuper = dataframes[dataframes['store_type'] == 'supermarket']
    storesuper = storesuper[['time', 'store_type', 'counts', 'I']]
    storesuper = storesuper.to_numpy()
    s = {}
    supermarkets = pd.DataFrame(columns = ['item_type', 'item_name', 'amount', 'category'])
    for timing, storetype, counts, i in storesuper:
        s[i] = pd.DataFrame(supermarket(dataframes, counts, timing))     
    s[i] = s[index]
    return s[index]

                
def bakeries(dataframes, index):
    storebake = dataframes[dataframes['store_type'] == 'bakery']
    storebake = storebake[['store_type', 'counts', 'I']]
    storebake = storebake.to_numpy()
    ba = {}
    supermarkets = pd.DataFrame(columns = ['item_type', 'item_name', 'amount', 'category'])
    for storetype, counts, i in storebake:
        ba[i] = pd.DataFrame(bakery(dataframes, counts))     
    ba[i] = ba[index]
    return ba[index]

def butchers(dataframes, index):
    #butcher
    storebutch = dataframes[dataframes['store_type'] == 'butcher']
    storebutch = storebutch[['store_type', 'counts', 'I']]
    storebutch = storebutch.to_numpy()
    bu = {}
    butchers = pd.DataFrame(columns = ['item_type', 'item_name', 'amount', 'category'])
    for storetype, counts, i  in storebutch:
        if storetype == 'butcher':
            bu[i] = pd.DataFrame(butcher(dataframes, counts))
    return bu[index]
    
def drugstores(dataframes, index):
    #drugstore
    storedrug = dataframes[dataframes['store_type'] == 'drugstore']
    storedrug = storedrug[['store_type', 'counts', 'I']]
    storedrug = storedrug.to_numpy()
    d = {}
    drugstores = pd.DataFrame(columns = ['item_type', 'item_name', 'amount', 'category'])
    for storetype, counts, i  in storedrug:
        if storetype == 'butcher':
            d[i] = pd.DataFrame(drugstore(dataframes, counts))
    return d[index]

def furnstores(dataframes, index):
        #furniture store
    storefurn = dataframes[dataframes['store_type'] == 'furniture store']
    storefurn = storefurn[['store_type', 'counts', 'I']]
    storefurn = storefurn.to_numpy()
    f = {}
    furnstores = pd.DataFrame(columns = ['item_type', 'item_name', 'amount', 'category'])
    for storetype, counts, i  in storefurn:
        if storetype == 'butcher':
            f[i] = pd.DataFrame(furniturestore(dataframes, counts))
    return f[index]