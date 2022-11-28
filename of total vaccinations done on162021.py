#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
#from pandasql import sqldf

df=pd.read_csv('https://raw.githubusercontent.com/tarikkranda/pi_datasets/main/country_vaccination_stats.csv')

#What is the number of total vaccinations done on 1/6/2021 (MM/DD/YYYY)by considering missing values imputed version of dataset? 
df['date'] = pd.to_datetime('20210601', format='%Y%m%d', errors='ignore')

#calculate sum of daily_vaccinations
df.groupby(df['date'])['daily_vaccinations'].sum()


# In[ ]:





# In[ ]:




