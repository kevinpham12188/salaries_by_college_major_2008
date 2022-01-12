#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv("/Users/macos/PycharmProjects/Day 71 - Data Exploring/salaries_by_college_major.csv")


# In[2]:


df.head()


# In[3]:


df.shape


# In[4]:


df.columns


# In[5]:


df.isna()


# In[6]:


df.tail()


# In[7]:


clean_df = df.dropna()
clean_df.tail()


# In[8]:


clean_df["Starting Median Salary"].max()


# In[9]:


clean_df["Starting Median Salary"].idxmax()


# In[10]:


clean_df["Undergraduate Major"][43]


# In[11]:


clean_df["Mid-Career Median Salary"].max()


# In[12]:


clean_df["Mid-Career Median Salary"].idxmax()


# In[13]:


clean_df.loc[8]


# In[14]:


clean_df["Starting Median Salary"].min()


# In[15]:


clean_df["Starting Median Salary"].idxmin()


# In[16]:


clean_df.loc[49]


# In[17]:


clean_df["Mid-Career Median Salary"].min()


# In[18]:


clean_df["Mid-Career Median Salary"].idxmin()


# In[19]:


clean_df.loc[18]


# In[20]:


spread_col = clean_df["Mid-Career 90th Percentile Salary"] - clean_df["Mid-Career 10th Percentile Salary"]
clean_df.insert(1, "Spread", spread_col)


# In[22]:


#Sorting by the Lowest Spread
low_risk = clean_df.sort_values("Spread")
low_risk[["Undergraduate Major", "Spread"]].head()


# In[24]:


high_risk = clean_df.sort_values("Spread", ascending=False)
high_risk[["Undergraduate Major", "Spread"]].head()


# In[26]:


high_potential = clean_df.sort_values("Mid-Career 90th Percentile Salary", ascending=False)
high_potential[["Undergraduate Major", "Mid-Career 90th Percentile Salary"]].head()


# In[27]:


clean_df.groupby("Group").count()


# In[30]:


# pd.options.display.float_format = '{:,.2f}'.format
round(clean_df.groupby("Group").mean(),2)

