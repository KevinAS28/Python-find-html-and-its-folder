import os
import sys
import re
import shutil
import copas1
import copas
def check_args():
    if (not(len(sys.argv)>1)):
        print("Please input the start dir")
        sys.exit(1)
    
    print("Processing...Please Wait")
#check_args()
def find_offline():
    for root, dirs, files in os.walk(sys.argv[1], topdown=False):
        index = []
        error = []    
        for i in dirs:
            i = os.path.join(i, root)
            try:
                os.chdir(i)
                for a in os.listdir():
                    if (a.endswith(".html")):
                        if (not(i in index)):
                            index.append(i)
                        break
            except Exception as err:
                error.append(str(err))
        for i in error:
            print("Error: ", i)
        print("Result: \n")            
        for i in index:
            print(i)        

def cphtml(dirs, dest):
    inside = os.listdir(dirs)
    html = []
    folder = []
    #dest = "/root/Downloads/tor-browser-linux64-7.0.4_en-US/tor-browser_en-US/Browser/Downloads/"
    #dest = "/root/bagi/offline/"
    for i in inside:
        if re.match("((.)*)[\.](htm)", i):
            a = i.replace(".htm", "_files")
            try:
                inside.index(a)
                folder.append(os.path.join(dirs, a))
                html.append(os.path.join(dirs, i))
            except:
                pass
    for i in html:
        print(copas1.cpfile(i, os.path.join(dest, os.path.basename(i))))
    for i in folder:
        print(copas1.cpfol(i, os.path.join(dest, os.path.basename(i))))

        

    
    
#cphtml("/media/root/windows10/Users/kevin/Pictures/")
cphtml(input("where are the html offline dirs? "), input("to where you want to copy them?"))               
            
                
                
        
    
        
