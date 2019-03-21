import shutil
def cpfile(dari, tujuan):
 #try:
  print("Copying", dari, "ke", tujuan, "...")
  open(tujuan, "w+")
  with open(dari, "rb") as oke:
   oke = oke.read()
   with open(tujuan, "wb") as eko:
    eko.write(oke)
  return True
 #except:
 # return False
def cpfol(dari, tujuan):
 shutil.copytree(dari, tujuan)
 return True
