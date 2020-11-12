#!/usr/bin/env python
# coding: utf-8

# In[1]:


conda install pandas_profiling


# In[2]:


import pandas as pd
import numpy as np


# In[3]:


matches = pd.read_csv('./Downloads/work/matches.csv')

matches


# In[4]:


df=matches[(matches['team1'] == 'Kings XI Punjab') & (matches['team2'] == 'Royal Challengers Bangalore')]

df


# In[5]:


dr=matches[(matches['team1'] == 'Royal Challengers Bangalore') & (matches['team2'] == 'Kings XI Punjab')]

dr


# In[6]:


noofwins = df.pivot_table(index=['winner'], aggfunc='size')
print (noofwins)


# In[7]:


noofwins = dr.pivot_table(index=['winner'], aggfunc='size')
print (noofwins)


# In[8]:


deliveries = pd.read_csv('./Downloads/work/deliveries.csv')

deliveries


# In[9]:


dr=deliveries[(deliveries['batting_team'] == 'Kings XI Punjab') & (deliveries['bowling_team'] == 'Royal Challengers Bangalore')]
dr


# In[10]:


out = dr.pivot_table(index=['player_dismissed'], aggfunc='size')
print (out)


# In[11]:


import statistics
average = statistics.mean(out)
average


# In[12]:


noball = dr.pivot_table(index=['noball_runs'], aggfunc='size')
print (noball)


# In[13]:


df=deliveries[(deliveries['batting_team'] == 'Royal Challengers Bangalore') & (deliveries['bowling_team'] == 'Kings XI Punjab')]
df


# In[14]:


noball = df.pivot_table(index=['noball_runs'], aggfunc='size')
print (noball)


# In[15]:


dp=df[(df['batsman'] == 'AB de Villiers') & (df['non_striker'] == 'Virat Kohli')]
dp


# In[16]:


dp=df[(df['batsman'] == 'Virat Kohli') & (df['non_striker'] == 'AB de Villiers')]
dp


# In[17]:


noofrun = df.pivot_table(index=['total_runs'], aggfunc='size')
print (noofrun)


# In[18]:


noofrun = dr.pivot_table(index=['total_runs'], aggfunc='size')
print (noofrun)


# In[ ]:




