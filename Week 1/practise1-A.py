#!/usr/bin/env python
# coding: utf-8

# In[6]:


greeting= "hi"
name= input("what is your name?") 
n1=int(input("enter 1st number"))
n2=int(input("enter 2nd number"))
summ=n1+n2
sub=n1-n2
mul=n1*n2
dev=n1/n2
rem=n1%n2
exp=n1**n2
print(greeting + " Mr/Mrs " + name)
print("The sum of " + str(n1) + " and " + str(n2) + " equals " + str(summ) )
print("The sub of " + str(n1) + " and " + str(n2) + " equals " + str(sub) )
print("The mul of " + str(n1) + " and " + str(n2) + " equals " + str(mul) )
print("The dev of " + str(n1) + " and " + str(n2) + " equals " + str(dev) )
print("The rem of " + str(n1) + " and " + str(n2) + " equals " + str(rem) )
print("The exp of " + str(n1) + " and " + str(n2) + " equals " + str(exp) )

