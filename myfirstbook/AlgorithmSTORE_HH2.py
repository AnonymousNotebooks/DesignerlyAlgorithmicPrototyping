#!/usr/bin/env python
# coding: utf-8

# ## 2: SECOND ALGORITHM - WHERE WILL THEY SHOP?
# 
# Outcome (example):
# 1. input: Monday,Tuesday...
# 2. output: store name X,Y...

# ### Import libraries 

# In[20]:


# %matplotlib notebook
get_ipython().run_line_magic('matplotlib', 'inline')
#Pandas is a software library written for the Python programming language for data manipulation and analysis.
import pandas as pd
#NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays
import numpy as np
# Matplotlib is a plotting library for python and pyplot gives us a MatLab like plotting framework. We will use this in our plotter function to plot data.
import matplotlib.pyplot as plt
#Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics
import seaborn as sns
import dataframe_image as dfi
from datetime import time
import matplotlib.dates as mdates
from matplotlib.ticker import StrMethodFormatter
from matplotlib.pyplot import figure

class bcolors:
    WARNING = '\033[91m'
    BOLD = '\033[1m'
# ### Load and view data 

# In[21]:


# data for HH
df = pd.read_csv (r"C:\Users\20204113\OneDrive - TU Eindhoven\2_Research\1_Groceries\DATA\9th week - narrative (3rd attempt)\HH2\df\df_HH2.csv")


# In[22]:


# data for different days vs stores
df_Mondays = pd.read_csv (r"C:\Users\20204113\OneDrive - TU Eindhoven\2_Research\1_Groceries\DATA\9th week - narrative (3rd attempt)\HH2\df\df_HH2_Mo.csv")
df_Tuesday = pd.read_csv (r"C:\Users\20204113\OneDrive - TU Eindhoven\2_Research\1_Groceries\DATA\9th week - narrative (3rd attempt)\HH2\df\df_HH2_Tu.csv")
df_Wednesday = pd.read_csv (r"C:\Users\20204113\OneDrive - TU Eindhoven\2_Research\1_Groceries\DATA\9th week - narrative (3rd attempt)\HH2\df\df_HH2_We.csv")
df_Thursday = pd.read_csv (r"C:\Users\20204113\OneDrive - TU Eindhoven\2_Research\1_Groceries\DATA\9th week - narrative (3rd attempt)\HH2\df\df_HH2_Th.csv")
df_Friday = pd.read_csv (r"C:\Users\20204113\OneDrive - TU Eindhoven\2_Research\1_Groceries\DATA\9th week - narrative (3rd attempt)\HH2\df\df_HH2_Fr.csv")
df_Saturday = pd.read_csv (r"C:\Users\20204113\OneDrive - TU Eindhoven\2_Research\1_Groceries\DATA\9th week - narrative (3rd attempt)\HH2\df\df_HH2_Sa.csv")
df_Sunday = pd.read_csv (r"C:\Users\20204113\OneDrive - TU Eindhoven\2_Research\1_Groceries\DATA\9th week - narrative (3rd attempt)\HH2\df\df_HH2_Su.csv")


# In[23]:

    # Function to generate #visits per day of the week
from AlgorithmDAYS_HH2 import beforeNY, AfterNY, daysAfterNY

    #Function to define the limits for total visits, days, same store and type per week
from AlgorithmCOUNTS_HH2 import CountTotalVisits, CountTotalDays, CountStoreName, CountTimePerDay, CountStoreType, CountTotalPerday, CountVisitsPerDay, CountTimingPerDay

    # Function to decide time (morning, noon. afternoon) per visited store
from AlgorithmTIMES_HH2 import AlbertHeijn, Okay, Delhaize, Carrefour, VersavelPoelman, Sys, Brabo, Ikea, Kruidvat
   
    # Function to decide amounts per visit & per week
from AlgorithmAMOUNT_HH2 import StoreAmount, WeekAmount, StoreCount, WeekCount


# # 1. SELECT STORE NAME

# In[24]:


#create random samples for this day based on the assigned weights
def Mondays(n):
    df_Monday = df_Mondays.sample(n=n, weights='weight', replace=True) 
    df_Monday = df_Monday.assign(day='Monday')
    del df_Monday['weight']

    return df_Monday


# In[25]:


Mondays(2)


# In[26]:


#create random samples for this day based on the assigned weights
def Tuesdays(n):
    df_Tuesdays = df_Tuesday.sample(n=n, weights='weight', replace=True)
    df_Tuesdays = df_Tuesdays.assign(day='Tuesday')
    del df_Tuesdays['weight']

    return df_Tuesdays


# In[27]:


#create random samples for this day based on the assigned weights
def Wednesdays(n):
    df_Wednesdays = df_Wednesday.sample(n=n, weights='weight', replace=True)
    df_Wednesdays = df_Wednesdays.assign(day='Wednesday')
    del df_Wednesdays['weight']

    return df_Wednesdays


# In[28]:


#create random samples for this day based on the assigned weights
def Thursdays(n):
    df_Thursdays = df_Thursday.sample(n=n, weights='weight', replace=True)
    df_Thursdays = df_Thursdays.assign(day='Thursday')
    del df_Thursdays['weight']

    return df_Thursdays


# In[29]:


#create random samples for this day based on the assigned weights
def Fridays(n):
    df_Fridays = df_Friday.sample(n=n, weights='weight', replace=True)
    df_Fridays = df_Fridays.assign(day='Friday')
    del df_Fridays['weight']

    return df_Fridays


# In[30]:


#create random samples for this day based on the assigned weights
def Saturdays(n):
    df_Saturdays = df_Saturday.sample(n=n, weights='weight', replace=True)
    df_Saturdays = df_Saturdays.assign(day='Saturday')
    del df_Saturdays['weight']

    return df_Saturdays


# In[31]:


#create random samples for this day based on the assigned weights
def Sundays(n):
    df_Sundays = df_Sunday.sample(n=n, weights='weight', replace=True)
    df_Sundays = df_Sundays.assign(day='Sunday')
    del df_Sundays['weight']

    return df_Sundays    

# New function for store per day

dataframe = pd.read_csv (r"C:\Users\20204113\OneDrive - TU Eindhoven\2_Research\1_Groceries\DATA\9th week - narrative (3rd attempt)\HH2\df\df_HH2.csv")


# df1 = daysAfterNY(dataframe)


def storeperday(dataframes):
    restart = True 

    while restart:

        ### 2. What STORE?
                    # identify counts for visits per weekday
        mo = int(dataframes["times"].values[0])
        tu = int(dataframes["times"].values[1])
        we = int (dataframes["times"].values[2])
        th = int (dataframes["times"].values[3])
        fr = int (dataframes["times"].values[4])
        sa = int (dataframes["times"].values[5])
        su = int (dataframes["times"].values[6])

            # Generate store names for the [previously identified] shopping dags + corresponding store type
        stores = [Mondays(mo), Tuesdays(tu), Wednesdays(we), Thursdays(th), Fridays(fr), Saturdays(sa), Sundays(su)]
            # create one df for all visited stores + day of the week
        stores = pd.concat(stores)


        ### 3. What TIME?

            # Identifier counts for store names per week
        AHt = (stores['store_name'] == 'Albert Heijn').sum()
        OKt = (stores['store_name'] == 'Okay').sum()
        DHt = (stores['store_name'] == 'Delhaize').sum()
        CFt = (stores['store_name'] == 'Carrefour').sum()
        VPt = (stores['store_name'] == 'Versavel Poelman').sum()
        SYt = (stores['store_name'] == 'Sys').sum()
        BRt = (stores['store_name'] == 'Brabo').sum()
        IKt = (stores['store_name'] == 'Ikea').sum()
        KRt = (stores['store_name'] == 'Kruidvat').sum()

            # Generate times per storename and compile in df with stores
        storetimes = [AlbertHeijn(AHt), Okay(OKt), Delhaize(DHt), Carrefour(CFt), VersavelPoelman(VPt), Sys(SYt), Brabo(BRt), Ikea(IKt), Kruidvat(KRt)]
        storetimes = pd.concat(storetimes)
        stores = pd.merge(stores, storetimes, on="store_name")

        ### CHECKPOINT: range for amount of stores per week.day

            # Check if the total STORE TYPES VISITED PER WEEK are within the normal range
        for storetype in dataframe['store_type']:
            typecount = stores[stores['store_type']==storetype]['store_type'].count()
            countstoretype = CountStoreType(storetype)
            minstoretype = countstoretype[0]
            maxstoretype = countstoretype[1]
            if typecount < minstoretype:
                print(f"{bcolors.WARNING}{bcolors.BOLD} RERUN - Too few store type:", storetype)
                restart = True
                break # force restart
            elif maxstoretype < typecount:
                print(f"{bcolors.WARNING}{bcolors.BOLD} RERUN - Too many store type:", storetype)
                restart = True
                break # force restart
            else:
                pass


            # Check if the total STORE NAMES VISITED PER WEEK are within the normal range
        for storename in dataframe['store_name']:
            namecount = stores[stores['store_name']==storename]['store_name'].count()
            countstorename = CountStoreName(storename)
            minstorename = countstorename[0]
            maxstorename = countstorename[1]
            if namecount < minstorename:
                print(f"{bcolors.WARNING}{bcolors.BOLD} RERUN - Too few store name:", storename)
                restart = True
                break # force restart
            elif maxstorename < namecount:
                print(f"{bcolors.WARNING}{bcolors.BOLD} RERUN - Too many store name:", storename)
                restart = True
                break # force restart
            else:
                pass


            # Check if the total STORES VISITED PER DAY are within the normal range
        for day in dataframe['day']:
            perdaycount = stores[stores['day']==day]['day'].count()
            CountTotalPerday = CountVisitsPerDay(day)
            minstoreperday = CountTotalPerday[0]
            maxstoreperday = CountTotalPerday[1]
            if namecount < minstoreperday:
                print(f"{bcolors.WARNING}{bcolors.BOLD} RERUN - Too few stores on:", day)
                restart = True
                break # force restart
            elif maxstoreperday < namecount:
                print(f"{bcolors.WARNING}{bcolors.BOLD} RERUN - Too many stores on:", day)
                restart = True
                break # force restart
            else:
                restart = False
                return stores
                break
                
                
# Itemcounts per store

def countsperstore(dataframes):
    storetime = dataframes[['store_name','time']]
    storetime

    restart = True 

    while restart:
        storecounts = []

        for store, time in storetime.itertuples(index=False):
            storecounts.append(StoreCount(store,time))

        dataframes['counts'] = storecounts

        # Check if the total ITEMS PER STORE are within the normal range
        for items in dataframe['item_type']:
            week9count = dataframes['counts'].sum()
            NormWeekCount = WeekCount()
            minWeekCount = NormWeekCount[0]
            maxWeekCount = NormWeekCount[1]
            if week9count < minWeekCount:
                print(f"{bcolors.WARNING}{bcolors.BOLD} RERUN - Too few items per storeNAME:", week9count)
                restart = True
                break # force restart
            elif maxWeekCount < week9count:
                print(f"{bcolors.WARNING}{bcolors.BOLD} RERUN - Too many items per storeNAME:", week9count)
                restart = True
                break # force restart
            else:
                restart = False
                return dataframes
                break