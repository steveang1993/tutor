# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 20:06:21 2020

@author: Steven
"""


while(True):
    x=input("input name:")
    while(True):
        for i in range(len(x)):
            if x[i]=='0' or x[i]=='1' or x[i]=='2' or x[i]=='3' or x[i]=='4' or x[i]=='5' or x[i]=='6' or x[i]=='7' or x[i]=='8' or x[i]=='9' or x[i]=='10' or x[i]=='+':
                print("name containing numbers")
            else:
                break
    else:
        print("Thank you")
    y=input("insert date of birth")
    listy=y.split('/')
    if y[2]%2==0 and y[0]>30:
        print("wrong input")
    else if y[0]>31:
        print("wrong input")
    

print(x)
print(y)