#!/usr/bin/env python
# coding: utf-8

# In[22]:


unit=input("select your input unit: 1 for C, and 2 for F")
temp=input("enter tempreture")
if unit==1: 
    print((temp*9/5)+32)
elif unit==2:
    print((temp-32)*5/9)
else:
    print("please select 1 or 2")
    


# In[ ]:




