# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 16:31:23 2017
@author: KD
Pallindrome

1. Create an empty string to hold the string
2. loop through each character in the input string
3. Inside the loop from zero to len(string) ie,length of string
    -if string character (string[i]) moving from left to right is equal to string characters moving from right to left then return true
    -else return false
4. At the point of function call if returned value is true:string is in pallindrome

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
    

