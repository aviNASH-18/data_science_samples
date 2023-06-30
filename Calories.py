#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[20]:


df=pd.read_csv('data.csv')
df


# In[21]:


df.isnull().sum()


# In[22]:


import numpy as np 


# In[26]:


x=np.mean(df['Calories'])
print(x)


# In[30]:


df=df.fillna(df.mean())
print(df.to_string())


# In[31]:


df.isnull().sum()


# In[32]:


from sklearn import linear_model


# In[50]:


A=df[['Duration','Maxpulse']]
print(A)


# In[43]:


b=df['Calories']
print(b)


# In[45]:


regr = linear_model.LinearRegression()
regr.fit(A, b)


# In[51]:


print(regr.coef_)


# In[52]:


predictedCalories=regr.predict([[62,140]])
print(predictedCalories)


# In[49]:


predictedCalories=regr.predict([[60,110]])
print(predictedCalories)


# In[ ]:




