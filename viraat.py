#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[9]:


pd.read_csv('final.csv')


# In[17]:


import pandas as pd
import plotly.express as px

df = pd.read_csv('final.csv')

fig = px.line(df, x = 'total', y = 'Match_No', title='Apple Share Prices over time (2014)')
fig.show()


# # Australia
# 

# In[38]:


df=pd.read_csv('final.csv')
Australia_mean=df[df.opponent=='Australia']
print(Australia_mean)


# In[39]:


Australia_mean=df[df.opponent=='Australia'].runs.mean()
print(Australia_mean)


# # SriLanka

# In[35]:


df=pd.read_csv('final.csv')
SriLanka_mean=df[df.opponent=='SriLanka']
print(SriLanka_mean)


# In[36]:


SriLanka_mean=df[df.opponent=='SriLanka'].runs.mean()
print(SriLanka_mean)


# #  England 

# In[33]:


England_mean=df[df.opponent=='England']
print(England_mean)


# In[34]:


England_mean=df[df.opponent=='England'].runs.mean()
print(England_mean)


# In[48]:


# NewZealand


# In[31]:


Zealand_mean=df[df.opponent=='NewZealand']
print(Zealand_mean)


# In[32]:


Zealand_mean=df[df.opponent=='NewZealand'].runs.mean()
print(Zealand_mean)


# In[52]:


# Bangladesh


# In[28]:


bangladesh_mean=df[df.opponent=='Bangladesh']
print(bangladesh_mean)


# In[54]:


df[df.opponent=='Bangladesh'].runs.mean()


# In[55]:


# Zimbabwe


# In[29]:


bangladesh_mean=zimbabwe=df[df.opponent=='Zimbabwe']
print(bangladesh_mean)


# In[27]:


zimbabwe=df[df.opponent=='Zimbabwe'].runs.mean()
print(zimbabwe)


# # SouthAfrica

# In[24]:


africa_mean=df[df.opponent=='SouthAfrica']
print(africa_mean)


# In[25]:


africa_mean=df[df.opponent=='SouthAfrica'].runs.mean()
print(africa_mean)


# # Ireland

# In[22]:


ireland_mean=df[df.opponent=='Ireland']
print(ireland_mean)


# In[23]:


ireland_mean=df[df.opponent=='Ireland'].runs.mean()
print(ireland_mean)


# # Pakistan

# In[20]:


pakistan_mean=df[df.opponent=='Pakistan']
print(pakistan_mean)


# In[21]:


pakistan_mean=df[df.opponent=='Pakistan'].runs.mean()
print(pakistan_mean)


# # WestIndies

# In[18]:


westindies=df[df.opponent=='WestIndies']
print(westindies)


# In[19]:


windies_mean=df[df.opponent=='WestIndies'].runs.mean()
print(windies_mean)


# In[48]:


import matplotlib.pyplot as plt
import numpy as np

y = np.array(["ireland_mean","windies_mean", "pakistan_mean", "africa_mean","bangladesh_mean","Zealand_mean","England_mean","Australia_mean"])
x = np.array([ 21.75,50.04109589041096, 42.35, 47.42622950819672,39.857142857142854,37.89320388349515,52.05714285714286,47.189473684210526,])

plt.bar(x,y,width = 0.7)
plt.show()


# In[ ]:





# In[ ]:




