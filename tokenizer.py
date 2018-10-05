 # -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 13:17:14 2017
@author: DELL1
"""
import re
def splitter(str):
    res = []
    res=re.split('\s+|\.|\$|\.|%|\n|#|\@|!|;|,',str)
    return(res)

token=[]
string_list=input("Please provide a input to tokenzier: ")
token=splitter(string_list)
print(token)
