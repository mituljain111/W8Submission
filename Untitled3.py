#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
car_details = pd.read_csv('cardetails.csv')


# In[2]:


car_details


# In[7]:


import matplotlib.pyplot as plt
 
boxplot = car_details.boxplot(figsize = (5,5))



# In[10]:


car_details.plot.scatter(x = 'price', y = 'mileage', s = 80); 


# In[23]:


import numpy as np

import plotly.express as px

fig = px.scatter(x=car_details['price'], y=df['mileage'])

fig.show()


# In[ ]:





# In[22]:


import pylab as py
sm.qqplot(car_details, line ='45') 
py.show() 


# In[ ]:




