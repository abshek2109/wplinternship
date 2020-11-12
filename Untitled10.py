#!/usr/bin/env python
# coding: utf-8

# In[1]:



import pandas as pd
import numpy as np

matches = pd.read_csv('./Downloads/work/matches.csv')

matches

df=matches[(matches['team1'] == 'Mumbai Indians') & (matches['team2'] == 'Kolkata Knight Riders')]

df

de=matches[(matches['team1'] == 'Kolkata Knight Riders') & (matches['team2'] == 'Mumbai Indians')]


# In[2]:


df


# In[3]:


de


# In[4]:


noofwins = de.pivot_table(index=['winner'], aggfunc='size')
print (noofwins)


# In[5]:


noofwins = df.pivot_table(index=['winner'], aggfunc='size')
print (noofwins)


# In[6]:


deliveries = pd.read_csv('./Downloads/work/deliveries.csv')

deliveries


# In[8]:


dr=deliveries[(deliveries['batting_team'] == 'Mumbai Indians') & (deliveries['over'] >= 6) & (deliveries['over'] <= 15) & (deliveries['bowling_team'] == 'Kolkata Knight Riders')]
dr


# In[9]:


import statistics
out = dr.pivot_table(index=['player_dismissed'], aggfunc='size')
print (out)
average = statistics.mean(out)


# In[10]:


dr=deliveries[(deliveries['batting_team'] == 'Kolkata Knight Riders') & (deliveries['bowling_team'] == 'Mumbai Indians')]
dr


# In[11]:


out = dr.pivot_table(index=['total_runs'], aggfunc='size')
print (out)


# In[14]:


dr=deliveries[(deliveries['batting_team'] == 'Mumbai Indians') & (deliveries['player_dismissed'] == 'RG Sharma') & (deliveries['bowling_team'] == 'Kolkata Knight Riders')]
dr


# In[15]:


outkind = dr.pivot_table(index=['dismissal_kind'], aggfunc='size')
print (outkind)


# In[ ]:




