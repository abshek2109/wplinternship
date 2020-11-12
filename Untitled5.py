#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[3]:


matches = pd.read_csv('./Downloads/work/matches.csv')


# In[4]:


matches


# In[5]:


matches[matches['winner'].isin(['Chennai Super Kings','Sunrisers Hyderabad'])]


# In[8]:


df=matches[(matches['team1'] == 'Chennai Super Kings') & (matches['team2'] == 'Sunrisers Hyderabad')]


# In[9]:


de=matches[(matches['team1'] == 'Sunrisers Hyderabad') & (matches['team2'] == 'Chennai Super Kings')]


# In[10]:


df


# In[11]:


de


# In[12]:


noofwins = df.pivot_table(index=['winner'], aggfunc='size')
print (noofwins)


# In[13]:


noofwins = de.pivot_table(index=['winner'], aggfunc='size')
print (noofwins)


# In[18]:


deliveries = pd.read_csv('./Downloads/work/deliveries.csv')


# In[19]:


deliveries


# In[20]:


dele = deliveries[(deliveries['batting_team'] == 'Sunrisers Hyderabad') & (deliveries['bowling_team'] == 'Chennai Super Kings')]


# In[21]:


delee = deliveries[(deliveries['batting_team'] == 'Chennai Super Kings') & (deliveries['bowling_team'] == 'Sunrisers Hyderabad')]


# In[22]:


dele


# In[23]:


delee


# In[24]:


wide = dele.pivot_table(index=['wide_runs'], aggfunc='size')
print (wide)


# In[25]:


widee = delee.pivot_table(index=['wide_runs'], aggfunc='size')
print (widee)


# In[27]:


out = delee.pivot_table(index=['player_dismissed'], aggfunc='size')
print (out)


# In[29]:


import statistics


# In[30]:


average = statistics.mean(out)


# In[31]:


average


# In[32]:


total = delee.pivot_table(index=['total_runs'], aggfunc='size')
print (total)


# In[33]:


average = statistics.mean(total)


# In[34]:


average


# In[35]:


total2 = dele.pivot_table(index=['total_runs'], aggfunc='size')
print (total2)


# In[36]:


average = statistics.mean(total2)


# In[37]:


average


# In[38]:


conda install -c anaconda pandas-profiling


# In[41]:


bat = dele.pivot_table(index=['batsman'], aggfunc='size')
print (bat)


# In[47]:


batt=dele.loc[dele['batsman'] == 'DA Warner']


# In[52]:


run = batt.pivot_table(index=['batsman_runs'], aggfunc='size')
print (run)


# In[53]:


average = statistics.mean(run)
average


# In[ ]:




