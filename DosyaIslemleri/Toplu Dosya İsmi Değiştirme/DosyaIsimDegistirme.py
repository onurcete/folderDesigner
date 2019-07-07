# Pythono3 code to rename multiple 
# files in a directory or folder 

# importing os module 
import os,time
from datetime import datetime


#liste halinde pathdeki dosya isimlerini tutar
print(os.listdir("/Users/onur.cete/Desktop/python/ÇALIŞMALAR/DosyaIslemleri/Toplu Dosya İsmi Değiştirme/Test"))


# Function to rename multiple files 
def main(): 
    i = 0
    a=[]
    b=[]
    dir="/Users/onur.cete/Desktop/python/ÇALIŞMALAR/DosyaIslemleri/Toplu Dosya İsmi Değiştirme/Test"
    
    for filename in os.listdir(dir): 
        dst ="x" + str(i) + ".txt"
        src = filename 
        dst = dst 
          
        # rename() function will 
        # rename all the files 
        os.chdir(dir)
        b.append([src,datetime.fromtimestamp(os.path.getmtime(filename)).strftime('%Y-%m-%d')])

        os.rename(src, dst) 

        #file creat and modifiy dates
        #print("Last modified: %s" % time.ctime(os.path.getmtime(filename)))
        #print("created: %s" % time.ctime(os.path.getctime(filename)))
        #print(datetime.fromtimestamp(os.path.getmtime(filename)).strftime('%Y-%m-%d %H:%M:%S'))
        
        
        a.append(datetime.fromtimestamp(os.path.getmtime(filename)).strftime('%Y-%m-%d'))

        

        i += 1
    print(a)
    print(b)
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 
    
