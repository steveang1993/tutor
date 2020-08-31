# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 20:02:02 2020

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
    y=input("insert email addr")
    name=y.split('@')[0]
    after=y.split('@')[1]
    def check_one_number():
        if any(i.isdigit() for i in name)==True:print("Your email is valid:",x)
        else:print("WRONG INPUT, your name must contain at least 1 number.")
    def check_after_d():
        lista=[]
        lista.append(after)
    if lista[0][:1]=='d' and lista[0][2:]==('.com' or '.co.id' or '.edu' or '.ac.id'):print("Your email is valid:",x)
    else:print("WRONG INPUT, after @ must be d.")
    check_one_number()
    check_after_d()

print(x)
print(y)