# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 17:07:54 2017
@author: kd
Create 2 empty strings as string1 and string2 : string1 is the original and string2 for checking if rotation is there
2. loop through both the strings to input the string
3. take length of string1 as l1 and string2 as l2
4. concatenate string1 to itself as string1= string1 + string1
5. If l1 is equal l2 
6. Check if string2 is substring of concatenated string1 ,Boolean = True
7. Else Boolean = false
8. If Boolean is true : string2 is rotation of string1

 To check substring in python : if string2 in string1
Or string1.find(string2) : which is true if string2 is in {concatenated} string1

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
            
