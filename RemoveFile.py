import os
import shutil
import time
from datetime import datetime

path="C:/Users/Santosh/Desktop/whiteHat/project99/30daysFile/"
days=30

seconds=days*24*60*60

systime=time.time() - seconds

if os.path.exists(path):
 fileList = os.listdir(path)

 for i in fileList:
  filejoin = os.path.join(path+i)
  ctime=os.stat(filejoin).st_ctime 
 
  
  if ctime < systime:
   os.remove(filejoin)

print("older files have been cleaned up")   

  
 
 
