# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 17:07:54 2017

@author: DELL1
"""
str=""
str=input("please enter the string :")
k=True

str2=""
str2=input("please enter the second string :")

l=len(str)
l2=len(str2)
str=str+str

if(l==l2):
    if str2 in str:
        k=True
    else:
        k=False
else:           
    k=False

if(k==True): 
    print("string is a rotation")
else:
    print("string is not a rotation")       
            