#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


matches = pd.read_csv('./Downloads/work/matches.csv')


# In[3]:


matches


# In[28]:


df=matches[(matches['team1'] == 'Delhi Daredevils') & (matches['team2'] == 'Rajasthan Royals')]


# In[29]:


df


# In[30]:


de=matches[(matches['team1'] == 'Rajasthan Royals') & (matches['team2'] == 'Delhi Daredevils')]


# In[31]:


de


# In[32]:


dr=matches[(matches['team1'] == 'Rajasthan Royals') & (matches['team2'] == 'Delhi Capitals')]


# In[33]:


dr


# In[34]:


noofwins = de.pivot_table(index=['winner'], aggfunc='size')
print (noofwins)


# In[35]:


noofwins = dr.pivot_table(index=['winner'], aggfunc='size')
print (noofwins)


# In[36]:


noofwins = df.pivot_table(index=['winner'], aggfunc='size')
print (noofwins)


# In[37]:


deliveries = pd.read_csv('./Downloads/work/deliveries.csv')


# In[38]:


deliveries


# In[44]:


dr=deliveries[(deliveries['batting_team'] == 'Delhi Capitals') & (deliveries['over'] <= 6) & (deliveries['bowling_team'] == 'Rajasthan Royals')]
dr


# In[45]:


noofruns = dr.pivot_table(index=['total_runs'], aggfunc='size')
print (noofruns)


# In[46]:


dr=deliveries[(deliveries['batting_team'] == 'Delhi Daredevils') & (deliveries['over'] <= 6) & (deliveries['bowling_team'] == 'Rajasthan Royals')]
dr


# In[48]:


noofrun = dr.pivot_table(index=['total_runs'], aggfunc='size')
print (noofrun)


# In[49]:


import statistics
average = statistics.mean(noofruns)
average


# In[50]:


average = statistics.mean(noofrun)
average


# In[53]:


dr=deliveries[(deliveries['batting_team'] == 'Rajasthan Royals') & (deliveries['bowling_team'] == 'Delhi Capitals')]
dr
bat = dr.pivot_table(index=['batsman'], aggfunc='size')
print (bat)


# In[55]:


batt=dr.loc[dr['batsman'] == 'SPD Smith']


# In[57]:


run = batt.pivot_table(index=['batsman_runs'], aggfunc='size')
print (run)


# In[61]:


wide = dr.pivot_table(index=['wide_runs'], aggfunc='size')
print (wide)


# In[58]:


dr=deliveries[(deliveries['batting_team'] == 'Rajasthan Royals') & (deliveries['bowling_team'] == 'Delhi Daredevils')]
dr
bat = dr.pivot_table(index=['batsman'], aggfunc='size')
print (bat)


# In[59]:


batt=dr.loc[dr['batsman'] == 'SPD Smith']


# In[60]:


run = batt.pivot_table(index=['batsman_runs'], aggfunc='size')
print (run)


# In[62]:


wide = dr.pivot_table(index=['wide_runs'], aggfunc='size')
print (wide)


# In[65]:


dr=deliveries[(deliveries['batting_team'] == 'Delhi Capitals') & (deliveries['bowling_team'] == 'Rajasthan Royals')]
dr
wide = dr.pivot_table(index=['wide_runs'], aggfunc='size')
print (wide)
out = dr.pivot_table(index=['player_dismissed'], aggfunc='size')
print (out)


# In[67]:


dr=deliveries[(deliveries['batting_team'] == 'Delhi Daredevils') & (deliveries['bowling_team'] == 'Rajasthan Royals')]
dr
wide = dr.pivot_table(index=['wide_runs'], aggfunc='size')
print (wide)
out = dr.pivot_table(index=['player_dismissed'], aggfunc='size')
print (out)
average = statistics.mean(out)


# In[68]:


average


# In[ ]:




