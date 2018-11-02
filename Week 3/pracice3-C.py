#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
files=os.listdir()
print(files)
old= input("select the old name of the file")
new= input("select the new name of the file")
os.rename(old,new)
print (files)

