# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 19:59:40 2020

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
    a=1
    while a>0:
      print("address input")
      print("do not use all capital letters, please start with the words: jl. or jalan")
      address=input("please input your address:")
    
      #output
      if len(address)>250:
        print("error, too much characters, please restart the program and reenter your address")
        a+=1
      else:
        if ("no." not in address) and ("No." not in address) and ("nomor" not in address) and ("Nomor" not in address):
          print("the address is not complete without specifying any number. please restart the program and reenter your address")
          a+=1
        else:
          if (address.startswith("jl.") or address.startswith("jalan") or address.startswith("Jl.") or address.startswith("Jalan")):
            print("thank you for submitting your address")
            break
          else:
            print("your address should start with either the word jl.,Jl,Jalan,or jalan. please restart the program end reenter your address")
            a+=1

print(x)
print(address)