#!/usr/bin/env python
# coding: utf-8

# # Introduction

# In[1]:


import pandas
from matplotlib import pyplot
get_ipython().magic('matplotlib inline')

recent_grads = pandas.read_csv("recent-grads.csv")
#print(recent_grads.shape)
print(recent_grads.iloc[0])
print(recent_grads.head())
print(recent_grads.tail())
print(recent_grads.describe())


# In[2]:


raw_data_count = recent_grads.shape[0]
raw_data_count


# In[3]:


recent_grads = recent_grads.dropna()
recent_grads


# In[4]:


cleaned_data_count = recent_grads.shape[0]
cleaned_data_count


# ## Pandas, Scatter Plots

# In[5]:


# scatter plot between Sample_size and Median
pyplot.scatter(recent_grads["Sample_size"], recent_grads["Median"])
pyplot.xlabel('Sample_size')
pyplot.ylabel('Median')
pyplot.show()


# In[6]:


# scatter plot between Sample_size and Unemployment_rate
pyplot.scatter(recent_grads["Sample_size"], recent_grads["Unemployment_rate"])
pyplot.xlabel('Sample_size')
pyplot.ylabel('Unemployment_rate')
pyplot.show()


# In[7]:


# scatter plot between Full_time and Median
pyplot.scatter(recent_grads["Full_time"], recent_grads["Median"])
pyplot.xlabel('Full_time')
pyplot.ylabel('Median')
pyplot.show()


# In[8]:


# scatter plot between ShareWomen and Unemployment_rate
pyplot.scatter(recent_grads["ShareWomen"], recent_grads["Unemployment_rate"])
pyplot.xlabel('ShareWomen')
pyplot.ylabel('Unemployment_rate')
pyplot.show()


# In[9]:


# scatter plot between Men and Median
pyplot.scatter(recent_grads["Men"], recent_grads["Median"])
pyplot.xlabel('Men')
pyplot.ylabel('Median')
pyplot.show()


# In[10]:


# scatter plot between Women and Median
pyplot.scatter(recent_grads["Women"], recent_grads["Median"])
pyplot.xlabel('Women')
pyplot.ylabel('Median')
pyplot.show()


# ## Pandas, Histograms

# In[11]:


# Histogram for Sample_Size
pyplot.hist(recent_grads["Sample_size"])
pyplot.show()


# In[12]:


# Histogram for Median
pyplot.hist(recent_grads["Median"])
pyplot.show()


# In[13]:


# Histogram for Employed
pyplot.hist(recent_grads["Employed"])
pyplot.show()


# In[14]:


# Histogram for Full_time data
pyplot.hist(recent_grads["Full_time"])
pyplot.show()


# In[15]:


# Histogram for ShareWomen
pyplot.hist(recent_grads["ShareWomen"])
pyplot.show()


# In[16]:


# Histogram for Unemployment_rate
pyplot.hist(recent_grads["Unemployment_rate"])
pyplot.show()


# In[17]:


# Histogram for Men
pyplot.hist(recent_grads["Men"])
pyplot.show()


# In[18]:


# Histogram for Women
pyplot.hist(recent_grads["Women"])
pyplot.show()


# ## Pandas, Scatter Matrix Plot

# In[19]:


#Scatter Matrix plot between Sample_size and Median
from pandas.plotting import scatter_matrix

scatter_matrix(recent_grads[["Sample_size", "Median"]], figsize=(6,6))


# In[20]:


# Scatter Matr
scatter_matrix(recent_grads[["Sample_size", "Median", "Unemployment_rate"]], figsize=(10,10))


# ## Pandas, Barplots

# In[21]:


# Barplot between Major and ShareWomen for data between row 0 and 10
from numpy import arange

bar_positions = arange(10) + 0.75
bar_heights = recent_grads["ShareWomen"][:10]
fig, ax = pyplot.subplots()
tick_positions = range(1, 11)

ax.bar(bar_positions, bar_heights, 0.5)
ax.set_xticks(tick_positions)
ax.set_xticklabels(recent_grads["Major"][0:10], rotation = 90.0)
pyplot.show()


# In[22]:


# Barplot between Major and ShareWomen for data between row 163 and 172
from numpy import arange

bar_positions = arange(9) + 0.75
bar_heights = recent_grads["ShareWomen"][163:172]
fig, ax = pyplot.subplots()
tick_positions = range(1, 10)

ax.bar(bar_positions, bar_heights, 0.5)
ax.set_xticks(tick_positions)
ax.set_xticklabels(recent_grads["Major"][163:172], rotation = 90.0)
pyplot.show()


# In[ ]:




