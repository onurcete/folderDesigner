
import os,time
import shutil
from datetime import datetime

dir=os.path.dirname(os.path.abspath(__file__)) + "/Test/" #.py nin çalıştığı dizini gösterir
#print('Dizin Giriniz:')
#dir = input()
#dir = dir +"/"

def yearAndFileList(): 
    i = 0
    fileYearList=[]
    fileNameList=[]
    
    #os.getcwd() # working directory gösterir
    
    for filename in os.listdir(dir): 
        os.chdir(dir)
        
        #if os.path.isfile(filename): 
        fileYearList.append(datetime.fromtimestamp(os.path.getmtime(filename)).strftime('%Y'))
        #elif os.path.isfile(filename): 
        fileNameList.append(filename)
        i += 1

    #file_list=list(dict.fromkeys(fileYearList))  #çoklayan kayıtları listeden siler
    fileYearList=list(set(fileYearList))  #çoklayan kayıtları listeden siler

    print(fileYearList)
    print(fileNameList)

    returnData=[fileYearList,fileNameList]
    print(returnData)
    return returnData

def createFolder(folderNames): 
    i = 0
    
    for yearName in folderNames:

        # define the name of the directory to be created
        path = dir+"/"+folderNames[i]

        try:  
            os.mkdir(path)
        except OSError:  
            print ("Creation of the directory %s failed" % path)
        else:  
            print ("Successfully created the directory %s " % path)
        os.chdir(dir)
        i += 1

def MoveFiles(FileNames): 

    i = 0
    for filename in FileNames: 
        os.chdir(dir)
        #if os.path.isfile(filename): 
        shutil.move(filename, dir+datetime.fromtimestamp(os.path.getmtime(filename)).strftime('%Y'))
        i += 1


if __name__ == '__main__': 

    x=yearAndFileList()
    folderNames=x[0]
    fileNames=x[1]

    createFolder(folderNames)
    #MoveFiles(fileNames)
    

    
