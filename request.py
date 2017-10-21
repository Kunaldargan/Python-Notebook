# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 02:00:47 2017

@author: DELL1
Beautiful Soup and Requests
"""
import requests
from bs4 import BeautifulSoup

url=''
url=input("Enter the Url :")
page=requests.get(url)
soup=BeautifulSoup(page.text,'html.parser')
for a in soup.find_all('p'):
    print(a.text)
"""    
Beautiful Soup, so rich and green,
  Waiting in a hot tureen!
  Who for such dainties would not stoop?
  Soup of the evening, beautiful Soup!
  Soup of the evening, beautiful Soup!
Beau--ootiful Soo--oop!
  Beau--ootiful Soo--oop!
  Soo--oop of the e--e--evening,
  Beautiful, beautiful Soup!
Beautiful Soup! Who cares for fish,
  Game or any other dish?
  Who would not give all else for two
  Pennyworth only of Beautiful Soup?
  Pennyworth only of beautiful Soup?
Beau--ootiful Soo--oop!
  Beau--ootiful Soo--oop!
  Soo--oop of the e--e--evening,
  Beautiful, beauti--FUL SOUP!"""

y=input("Do u want parse entire html tree :yes or no  " )

if(y=='yes'):
    print(soup.prettify())
else:
    exit
    
