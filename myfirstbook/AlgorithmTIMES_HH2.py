#!/usr/bin/env python
# coding: utf-8

# ## 3: THIRD ALGORITHM - AT WHAT TIME WILL THEY SHOP?
# 
# Outcome (example):
# 1. input: Monday,Tuesday...
# 2. output: noon/morning/afternoon

# ### Import libraries 

# In[37]:


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


# ### Load and view data 

# In[38]:


# data for HH
df = pd.read_csv (r"C:\Users\20204113\OneDrive - TU Eindhoven\2_Research\1_Groceries\DATA\9th week - narrative (3rd attempt)\HH2\df\df_HH2.csv")


# In[39]:


# data for different days vs stores
df_AlbertHeijns = pd.read_csv (r"C:\Users\20204113\OneDrive - TU Eindhoven\2_Research\1_Groceries\DATA\9th week - narrative (3rd attempt)\HH2\df\df_HH2_AHTime.csv")
df_Syss = pd.read_csv (r"C:\Users\20204113\OneDrive - TU Eindhoven\2_Research\1_Groceries\DATA\9th week - narrative (3rd attempt)\HH2\df\df_HH2_SYTime.csv")
df_Okays = pd.read_csv (r"C:\Users\20204113\OneDrive - TU Eindhoven\2_Research\1_Groceries\DATA\9th week - narrative (3rd attempt)\HH2\df\df_HH2_OKTime.csv")
df_Delhaizes = pd.read_csv (r"C:\Users\20204113\OneDrive - TU Eindhoven\2_Research\1_Groceries\DATA\9th week - narrative (3rd attempt)\HH2\df\df_HH2_DETime.csv")
df_Versavels = pd.read_csv (r"C:\Users\20204113\OneDrive - TU Eindhoven\2_Research\1_Groceries\DATA\9th week - narrative (3rd attempt)\HH2\df\df_HH2_VETime.csv")
df_Kruidvats = pd.read_csv (r"C:\Users\20204113\OneDrive - TU Eindhoven\2_Research\1_Groceries\DATA\9th week - narrative (3rd attempt)\HH2\df\df_HH2_KRTime.csv")
df_Brabos = pd.read_csv (r"C:\Users\20204113\OneDrive - TU Eindhoven\2_Research\1_Groceries\DATA\9th week - narrative (3rd attempt)\HH2\df\df_HH2_BRTime.csv")
df_Ikeas = pd.read_csv (r"C:\Users\20204113\OneDrive - TU Eindhoven\2_Research\1_Groceries\DATA\9th week - narrative (3rd attempt)\HH2\df\df_HH2_IKTime.csv")
df_Carrefours = pd.read_csv (r"C:\Users\20204113\OneDrive - TU Eindhoven\2_Research\1_Groceries\DATA\9th week - narrative (3rd attempt)\HH2\df\df_HH2_CATime.csv")


# # SELECT TIME

# In[40]:


#create random samples for this day based on the assigned weights
def AlbertHeijn(n):
    df_AlbertHeijn = df_AlbertHeijns.sample(n=n, weights='weight', replace=True) 
    del df_AlbertHeijn['weight']
    df_AlbertHeijn = df_AlbertHeijn.assign(store_name='Albert Heijn')
    return df_AlbertHeijn


# In[41]:


#create random samples for this day based on the assigned weights
def Okay(n):
    df_Okay = df_Okays.sample(n=n, weights='weight', replace=True)
    del df_Okay['weight']
    df_Okay = df_Okay.assign(store_name='Okay')
    return df_Okay


# In[42]:


#create random samples for this day based on the assigned weights
def Delhaize(n):
    df_Delhaize = df_Delhaizes.sample(n=n, weights='weight', replace=True)
    del df_Delhaize['weight']
    df_Delhaize = df_Delhaize.assign(store_name='Delhaize')
    return df_Delhaize


# In[43]:


#create random samples for this day based on the assigned weights
def Carrefour(n):
    df_Carrefour = df_Carrefours.sample(n=n, weights='weight', replace=True)
    del df_Carrefour['weight']
    df_Carrefour = df_Carrefour.assign(store_name='Carrefour')
    return df_Carrefour


# In[44]:


#create random samples for this day based on the assigned weights
def VersavelPoelman(n):
    df_Versavel = df_Versavels.sample(n=n, weights='weight', replace=True)
    del df_Versavel['weight']
    df_Versavel = df_Versavel.assign(store_name='Versavel Poelman')
    return df_Versavel


# In[45]:


#create random samples for this day based on the assigned weights
def Sys(n):
    df_Sys = df_Syss.sample(n=n, weights='weight', replace=True)
    del df_Sys['weight']
    df_Sys = df_Sys.assign(store_name='Sys')
    return df_Sys


# In[46]:


#create random samples for this day based on the assigned weights
def Brabo(n):
    df_Brabo = df_Brabos.sample(n=n, weights='weight', replace=True)
    del df_Brabo['weight']
    df_Brabo = df_Brabo.assign(store_name='Brabo')
    return df_Brabo


# In[47]:


#create random samples for this day based on the assigned weights
def Kruidvat(n):
    df_Kruidvat = df_Kruidvats.sample(n=n, weights='weight', replace=True)
    del df_Kruidvat['weight']
    df_Kruidvat = df_Kruidvat.assign(store_name='Kruidvat')
    return df_Kruidvat


# In[48]:


#create random samples for this day based on the assigned weights
def Ikea(n):
    df_Ikea = df_Ikeas.sample(n=n, weights='weight', replace=True)
    del df_Ikea['weight']
    df_Ikea = df_Ikea.assign(store_name='Ikea')
    return df_Ikea


# In[49]: