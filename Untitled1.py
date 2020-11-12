#!/usr/bin/env python
# coding: utf-8

# # Analysis of match between KKR and CSK

# In[1]:


# Importing necessary library

import pandas as pd
import numpy as np


# In[2]:


# Import and Read data from dataset
matches = pd.read_csv('./matches.csv')

matches


# In[4]:


#create a dataframe for the match
df=matches[(matches['team1'] == 'Chennai Super Kings') & (matches['team2'] == 'Kolkata Knight Riders')]

df


# In[5]:


#create a dataframe for the match
de=matches[(matches['team1'] == 'Kolkata Knight Riders') & (matches['team2'] == 'Chennai Super Kings')]


de


# In[6]:


#checking for number of wins by each team

noofwins = de.pivot_table(index=['winner'], aggfunc='size')
print (noofwins)


# In[7]:


#checking for number of wins by each team

noofwins = df.pivot_table(index=['winner'], aggfunc='size')
print (noofwins)


# In[8]:


#importing and reading dataset 

deliveries = pd.read_csv('./deliveries.csv')

deliveries


# In[13]:


#creating the dataframe for match


dr=deliveries[(deliveries['batting_team'] == 'Kolkata Knight Riders') & (deliveries['bowling_team'] == 'Chennai Super Kings')]

dr


# In[14]:


# finding the bowlers name

bowl = dr.pivot_table(index=['bowler'], aggfunc='size')
print (bowl)


# In[16]:


#creating dataframe for chahar bowling
deliveries_by_chahar=dr[(dr['bowler'] == 'DL Chahar') ]

deliveries_by_chahar


# #From above result is found that chahar took 12 balls,22 balls,34 balls respectively to get wickets

# In[23]:


# checking the noballs frequency for CSK bowling

noball = dr.pivot_table(index=['noball_runs'], aggfunc='size')

print (noball)


# #from above result is found that the no of no balls is very less 

# In[24]:


#creating dataframe for batting team CSK

dq=deliveries[(deliveries['batting_team'] == 'Chennai Super Kings') & (deliveries['bowling_team'] == 'Kolkata Knight Riders')]

dq


# In[25]:


# checking the noballs frequency for KKR bowling

noball = dq.pivot_table(index=['noball_runs'], aggfunc='size')

print (noball)


# #from above result is found that the no of no balls is very less

# In[ ]:




