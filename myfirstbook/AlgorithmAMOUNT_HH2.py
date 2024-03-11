#!/usr/bin/env python
# coding: utf-8

# ## 4: FOURTH ALGORITHM - FROM WHAT CATEGORIES?
# 
# Outcome (example):
# 1. input: DAY, TIME, STORE
# 2. output: CATEGORIES

# ### Import libraries 

# In[106]:


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
import random
class bcolors:
    WARNING = '\033[91m'
    BOLD = '\033[1m'


# ### Load and view data 

# In[107]:


df = pd.read_csv (r"C:\Users\20204113\OneDrive - TU Eindhoven\2_Research\1_Groceries\DATA\9th week - narrative (3rd attempt)\HH2\df\df_HH2.csv")


# In[108]:


df['time'] = df['time'].replace(['afternoon', 'evening'], 'afternoon')


# In[109]:


df_orders = df[['order_ID', 'week', 'store_name', 'storename_num', 'store_type', 'storetype_num','day', 'day_num', 'time', 'time_num', 'timestamp', 'times', 'dates', 'times_min', 'dates_days', 'order_amount', 'order_price']]
df_orders = df_orders.drop_duplicates()


# # Function (store as option)

# In[149]:


def StoreAmount(storename, time):
    df_store = df[df['store_name'] == storename]
    if (storename == 'Albert Heijn') & (time != 'afternoon'):
        df_store = df_store[df_store['time'] != 'afternoon']
        df_AHm = df_store.groupby(['order_ID'])['amount'].sum()
        df_AHm = pd.DataFrame (df_AHm)
        df_AHm = df_AHm.reset_index()
        min = df_AHm.min(axis=0)['amount']
        max = df_AHm.max(axis=0)['amount']
        return random.randint(min, max)
    elif (storename == 'Albert Heijn') & (time == 'afternoon'):
        df_store = df_store[df_store['time'] == 'afternoon']
        df_AHm = df_store.groupby(['order_ID'])['amount'].sum()
        df_AHm = pd.DataFrame (df_AHm)
        df_AHm = df_AHm.reset_index()
        min = df_AHm.min(axis=0)['amount']
        max = df_AHm.max(axis=0)['amount']
        return random.randint(min, max)
    else:
        df_store = df_store.groupby(['order_ID'])['amount'].sum()
        df_store = pd.DataFrame (df_store)
        df_store = df_store.reset_index()        
        min = df_store.min(axis=0)['amount']
        max = df_store.max(axis=0)['amount']
        return random.randint(min, max)

def StoreCount(storename, time):
    df_store = df[df['store_name'] == storename]
    if (storename == 'Albert Heijn') & (time != 'afternoon'):
        df_store = df_store[df_store['time'] != 'afternoon']
        df_AHm = df_store.groupby(['order_ID'])['amount'].count()
        df_AHm = pd.DataFrame (df_AHm)
        df_AHm = df_AHm.reset_index()
        min = df_AHm.min(axis=0)['amount']
        max = df_AHm.max(axis=0)['amount']
        return random.randint(min, max)
    elif (storename == 'Albert Heijn') & (time == 'afternoon'):
        df_store = df_store[df_store['time'] == 'afternoon']
        df_AHm = df_store.groupby(['order_ID'])['amount'].count()
        df_AHm = pd.DataFrame (df_AHm)
        df_AHm = df_AHm.reset_index()
        min = df_AHm.min(axis=0)['amount']
        max = df_AHm.max(axis=0)['amount']
        return random.randint(min, max)
    else:
        df_store = df_store.groupby(['order_ID'])['amount'].count()
        df_store = pd.DataFrame (df_store)
        df_store = df_store.reset_index()        
        min = df_store.min(axis=0)['amount']
        max = df_store.max(axis=0)['amount']
        return random.randint(min, max)

# In[150]:


StoreAmount('Delhaize', 'morning')


# # For the entire week

# In[110]:


def WeekAmount():
    df_amount = df_orders.groupby(['week'])['order_amount'].sum()
    df_amount = pd.DataFrame (df_amount)
    df_amount = df_amount.reset_index()

    min = df_amount.min(axis=0)['order_amount']
    max = df_amount.max(axis=0)['order_amount']
    return (min,max)

def WeekCount():
    df_count = df.groupby(['week'])['amount'].count()
    df_count = pd.DataFrame (df_count)
    df_count = df_count.reset_index()

    min = df_count.min(axis=0)['amount']
    max = df_count.max(axis=0)['amount']
    return (min,max)


def CatCount():
    df_count = df.groupby(['week'])['category'].nunique()
    df_count = pd.DataFrame (df_count)
    df_count = df_count.reset_index()

    min = df_count.min(axis=0)['category']
    max = df_count.max(axis=0)['category']
    return (min,max)


# group per period
BeforeNY = df.copy()
BeforeNY = BeforeNY[BeforeNY['week'] < 5]

AfterNY = df.copy()
AfterNY = AfterNY[AfterNY['week'] > 4]


def PerCatCount(category):
    data = {'week': [5,6,7,8]}
    weeks = pd.DataFrame(data)
    df_cat = AfterNY[AfterNY['category'] == category]
    df_cat = df_cat.groupby(['week'])['amount'].count()
    df_cat = pd.DataFrame (df_cat)
    df_cat = df_cat.reset_index() 
    df_cat = weeks.merge(df_cat, how='left').fillna(0)
    min = df_cat.min(axis=0)['amount']
    max = df_cat.max(axis=0)['amount']
    return (min, max)

# for entire period
def PerCatCountALL(category):
    data = {'week': [1,2,3,4,5,6,7,8]}
    weeks = pd.DataFrame(data)
    df_cat = df[df['category'] == category]
    df_cat = df_cat.groupby(['week'])['amount'].count()
    df_cat = pd.DataFrame (df_cat)
    df_cat = df_cat.reset_index() 
    df_cat = weeks.merge(df_cat, how='left').fillna(0)
    min = df_cat.min(axis=0)['amount']
    max = df_cat.max(axis=0)['amount']
    return (min, max)


# PER STORE TYPE
def PerCatCountSTORE(category, storetype):
    data = {'order_ID': range(1,39)}
    orderID = pd.DataFrame(data)
    df_cat = df[df['store_type'] == storetype]
    df_cat = df_cat[df_cat['category'] == category]
    df_cat = df_cat.groupby(['order_ID'])['amount'].count()
    df_cat = pd.DataFrame (df_cat)
    df_cat = df_cat.reset_index() 
    df_cat = orderID.merge(df_cat, how='left').fillna(0)
    min = df_cat.min(axis=0)['amount']
    max = df_cat.max(axis=0)['amount']
    return (min, max)