#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#     Loading The Dataset

# In[2]:


# Movies Data
movie_data = pd.read_csv("Netflix_Dataset_Movie.csv")
movie_data.head()


# In[4]:


# Rating Data
rating_data = pd.read_csv("Netflix_Dataset_Rating.csv")
rating_data.head()


# In[5]:


# User Data
user_data = pd.read_csv("User_Data.csv")
user_data.head()


# In[6]:


movie_data.info()


# In[8]:


movie_data.describe()


# In[9]:


movie_data.isnull()


# In[10]:


movie_data.isnull().sum()


# In[11]:


rating_data.isnull().sum()


# In[12]:


user_data.isnull().sum()


#     Combining all datasets

# In[13]:


movies_df = pd.concat([movie_data,rating_data,user_data],axis=1)


# In[14]:


movies_df.head()


# In[16]:


## Checking Null Values
movies_df.isnull().sum()


# In[18]:


#dropping NA's

movies_df.dropna()


# #    Removing Unwanted Columns

# In[19]:


movies_df = movies_df.drop(columns=['Movie_ID','User_ID','EstimatedSalary',
                                   'Purchased'])


# In[21]:


movies_df.head()


# In[22]:


movies_df.isnull().sum()


# In[23]:


movies_df = movies_df.dropna()
movies_df.head()


# In[24]:


movies_df.isnull().sum()


# In[26]:


movies_df.shape


# In[27]:


movies_df.to_excel("movie_rating.xlsx",sheet_name='data')


# In[28]:


movies_df[movies_df['Name'] == '20']


# In[ ]:




