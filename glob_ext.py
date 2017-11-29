from os import path

from glob import glob

def ext():
   l= glob(path.join("E:\\desktop\\Notebooks\\yearly stock data","*.csv"))
   print(l)
   
ext()   
