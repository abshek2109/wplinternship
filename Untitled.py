#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

matches = pd.read_csv('./matches.csv')

matches


# In[2]:



df=matches[(matches['team1'] == 'Kolkata Knight Riders') & (matches['team2'] == 'Royal Challengers Bangalore')]

df


# In[3]:


dr=matches[(matches['team1'] == 'Royal Challengers Bangalore') & (matches['team2'] == 'Kolkata Knight Riders')]

dr


# In[4]:


noofwins = df.pivot_table(index=['winner'], aggfunc='size')
print (noofwins)


# In[5]:



noofwins = dr.pivot_table(index=['winner'], aggfunc='size')
print (noofwins)


# In[8]:


deliveries = pd.read_csv('./deliveries.csv')

deliveries


# In[11]:


dr=deliveries[(deliveries['batting_team'] == 'Royal Challengers Bangalore') & (deliveries['bowling_team'] == 'Kolkata Knight Riders')]
dr


# In[15]:


dv=dr[(dr['over'] >= 16)]
dv


# In[16]:


noofrun = dv.pivot_table(index=['total_runs'], aggfunc='size')
print (noofrun)


# In[18]:


import statistics
average = statistics.mean(noofrun)
average


# In[19]:


dv=dr[(dr['over'] >= 4)]
dv


# In[20]:


out = dv.pivot_table(index=['player_dismissed'], aggfunc='size')
print (out)


# In[21]:


average = statistics.mean(out)
average


# In[ ]:




