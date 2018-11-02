#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests as rq

API="https://samples.openweathermap.org/data/2.5/forecast?"

additional_data = {
    "APPID" : "7bd564fc6c9bbb43d62c03c2585a9c91",
    "q": "Amman,Jo",
}

data = rq.get(API,params=additional_data).json()

print(data)

