# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 14:28:15 2017

@author: DELL1

filtered_sentence = [w for w in word_tokens if not w in stop_words]
is equivalent to:

filtered_sentence = []
for w in word_tokens:
    if not w in stopwords:
        filtered_sentence.append(w)
"""


import PyPDF2
import nltk 
from nltk.corpus import stopwords,wordnet
from nltk.tokenize import word_tokenize
 
stop_words = set(stopwords.words('english'))
filtered_sentence=[]
PDFfilename=[]
pg=""
t=[]
array=[]

def page_extract(pg):
    pfr = PyPDF2.PdfFileReader(open(pg, "rb")) #PdfFileReader object
    number_of_pages=int(pfr.getNumPages())
    for i in range(number_of_pages):
        pg+=pfr.getPage(i).extractText()
    return pg        


def word_extract(page):
    l=[]
    word_tokens = word_tokenize(page)
    filtered_words = [w for w in word_tokens if not w in stop_words]

    for i in range(len(filtered_words)):
        if wordnet.synsets(filtered_words[i]) and str.isalpha(filtered_words[i]) and len(filtered_words[i])>1 :#Comparing if word is non-English
            l.append(filtered_words[i])
            
    return l  

def compare(P):
    for i in range(len(P)):
       array=set(P[0]).intersection(P[i])
       print(array)
        #word[i].append(P[i])
    #print(word)
    
    
      

if __name__=='__main__':
    num = int(input("How many files you want to compare"))
    
    for n in range(0,num) :
        p=input("Enter Pdf file name")
        PDFfilename.append(p+".pdf")
        
    
    print(PDFfilename)
       
    for j in range(len(PDFfilename)):
        PDFfilename[j]=(page_extract(PDFfilename[j]))
   
    for k in range(len(PDFfilename)):
        PDFfilename[k]=(word_extract(PDFfilename[k]))
    compare(PDFfilename)  
    
        