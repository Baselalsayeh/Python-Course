#!/usr/bin/env python
# coding: utf-8

# In[28]:


state = ["irbid", "jarash", "ajlun", "amman", "zarqa", "mafraq", "madaba", "salt","tafeleh", "karak", "maan", "aqaba"]

for i in range (0,12):
     if state[i][0]=="a": 
        print(state[i])
        
print("***********************")
for i in range (0,12):
    if len(state[i])==5:
        print(state[i])
        


