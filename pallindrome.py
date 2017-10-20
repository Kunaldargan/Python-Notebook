# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 16:31:23 2017

@author: KD
Pallindrome
"""
str=""
str=input('Please enter string :')
 
l=len(str)

for i in range(l):
    if(str[i]==str[l-i]):
        k=1
    else:
        k=0
        
if(k!=0):
    print("Pallindrome")
else:
    print("not pallindrome")
    

