import os
import shutil
def cpany(src, dst):
  try:
   #for file 
   try:
     open(dst, "w+")
   except:
     pass
   try:
    with open(src, "rb") as oke:
       oke = oke.read()
       with open(dst, "wb") as eko:
         eko.write(oke)
   except:

    #if fail probally its folder
     try:
       os.remove(dst)
     except:
        yaudah = 0
     shutil.copytree(src, dst)  
  except Exception as Error:
    return Error
  return True
###not working yet
def cpindir(fol, dst):
  try:
    os.chdir(fol)
    to_copy = list(os.listdir())
  except:
    return False
  return True
