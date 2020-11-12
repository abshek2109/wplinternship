#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


matches = pd.read_csv('./Downloads/matches.csv')


# In[3]:


matches


# In[4]:


matches[matches['winner'].isin(['Kolkata Knight Riders','Royal Challengers Bangalore'])]


# In[5]:


matches[(matches['team1'] == 'Kolkata Knight Riders') & (matches['team2'] == 'Royal Challengers Bangalore')]


# In[6]:


df = matches[(matches['team1'] == 'Kolkata Knight Riders') & (matches['team2'] == 'Royal Challengers Bangalore')]
df


# In[7]:


noofwins = df.pivot_table(index=['winner'], aggfunc='size')
print (noofwins)


# In[8]:


winningtoss = df.pivot_table(index=['toss_winner'], aggfunc='size')
print (winningtoss)


# In[9]:


tosswinnerdecision = df.pivot_table(index=['toss_decision'], aggfunc='size')
print (tosswinnerdecision)


# In[10]:


deliveries = pd.read_csv('./Downloads/deliveries.csv')


# In[11]:


deliveries


# In[12]:


dele = deliveries[(deliveries['batting_team'] == 'Kolkata Knight Riders') & (deliveries['bowling_team'] == 'Royal Challengers Bangalore')]
dele


# In[13]:


noballs = dele.pivot_table(index=['noball_runs'], aggfunc='size')
print (noballs)


# In[ ]:




