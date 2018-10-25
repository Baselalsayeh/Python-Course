#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def cur_conv(op,ammount):
    if op==1:
        print(ammount*1.41)
    elif op==2:
        print(ammount*7.96)
    elif op==3:
        print(ammount*0.71)
    elif op==4:
        print(ammount*5.65)
    elif op==5:
        print(ammount*0.13)
    elif op==6:
        print(ammount*0.18)




print("welcome to currency converter program")
print("1. JD TO USD")
print("2. JD TO TL")
print("3. USD TO JD")
print("4. USD TO TL")
print("5. TL TO JOD")
print("6. TL TO USD")
op = int(input("please select operation"))
ammount = int(input("please select the ammount"))
cur_conv(op,ammount)

