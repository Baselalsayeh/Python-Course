#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests as rq
forex = 'http://data.fixer.io/api/latest?access_key=9cc6f6a6c7ef48bc24127dbc0340c2b2&format=1'


forex_data = rq.get(forex).json()
print("available currencies are:")
available_currencies=[]
euro_rates= forex_data["rates"]

for item in forex_data["rates"]:
    print(item, end = ", ") 
    available_currencies.append(item)
    
base_curr = input("Choose a currency: ")

available_currencies.remove(base_curr)
print("Available to: ", available_currencies)
to_curr = input("Choose from the above: ")

amount = float(input("How many you want to convert: "))


result = (euro_rates[to_curr]/euro_rates[base_curr]) * amount

print(result)


