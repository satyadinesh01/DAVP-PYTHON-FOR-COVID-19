#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[3]:


import matplotlib.pyplot as plt


# In[4]:


import plotly.express as ps
import os


# In[5]:


os.getcwd()


# In[6]:


df=pd.read_csv(".csv")


# In[ ]:


df.shape


# In[ ]:


df.columns


# In[ ]:


df.info() #gives concise summary of dataframe


# In[ ]:


df.nunique()  #returns number of unique values in each column


# In[ ]:


df.nunique


# In[ ]:


#statistical summary
df.describe()


# In[ ]:


#to check whether null values are present
df.isnull().sum()


# In[ ]:


#3 Relationship analysis


# In[ ]:


correlation = df.corr()
correlation


# In[ ]:



df.T


# In[ ]:


df.T.shape


# In[ ]:





# In[7]:


#sorting data in ascending order
df.sort_values (['Confirmed Cases'], inplace=True, ascending=False)
df


# In[8]:


df.head()


# In[9]:


df.tail()


# In[10]:


plt.plot(["confirmed cases"])


# In[11]:


plt.plot(["Confirmed Cases","Active Cases","Cured/Discharged","Death"])
plt.title("covid 19 in india")
plt.show()


# In[12]:


plt.plot(["Confirmed Cases","Active Cases","Cured/Discharged","Death"],'o')


# In[13]:


plt.plot(["Confirmed Cases","Active Cases","Cured/Discharged","Death"],marker='o')


# In[14]:


plt.plot(["Confirmed Cases","Active Cases","Cured/Discharged","Death"],marker='*')


# In[15]:


plt.plot(["Confirmed Cases","Active Cases","Cured/Discharged","Death"],marker='*',mec='r',mfc='b')


# In[16]:


plt.plot(["Confirmed Cases","Active Cases","Cured/Discharged","Death"],marker='_',ms=20,mec='y',mfc='b')


# In[17]:


plt.plot(["Confirmed Cases","Active Cases","Cured/Discharged","Death"],marker='o',ms=20,mec='y',mfc='b')


# In[18]:


plt.plot(["Confirmed Cases","Active Cases","Cured/Discharged","Death"],'o:r',ms=20,mec='y',mfc='b')


# In[19]:


df.plot()


# In[ ]:





# In[ ]:





# In[20]:


import seaborn as sns


# In[ ]:





# In[ ]:





# In[ ]:





# In[21]:


#sorting data in ascending order
df.sort_values (['Confirmed Cases'], inplace=True, ascending=False)
df


# In[22]:


sns.displot(df['Confirmed Cases'])


# In[23]:


sns.displot(df['Active Cases'])


# In[24]:


sns.displot(df['Death'])


# In[ ]:





# In[25]:


x=df.head(10)["State/UT"]
y=df.head(10)["Confirmed Cases"]
plt.pie(df.head(10)["Confirmed Cases"],labels=x)
plt.legend(y)
plt.show()


# In[26]:


fig=ps.scatter_3d(df.head(10),"Confirmed Cases","Active Cases","Death","State/UT")
fig.show()


# In[27]:


plt.bar(df.head(10),"Death","State/UT")
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




