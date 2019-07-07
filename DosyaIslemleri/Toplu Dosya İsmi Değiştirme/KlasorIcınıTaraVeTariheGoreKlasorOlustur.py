
import os,time
import shutil
from datetime import datetime

def yearAndFileList(): 
    i = 0
    fileYearList=[]
    fileNameList=[]
    dir=os.path.dirname(os.path.abspath(__file__)) + "/Test" #.py nin çalıştığı dizini gösterir
    #os.getcwd() # working directory gösterir
    
    for filename in os.listdir(dir): 
        os.chdir(dir)
        
        fileYearList.append(datetime.fromtimestamp(os.path.getmtime(filename)).strftime('%Y'))
        fileNameList.append(filename)
        i += 1

    #file_list=list(dict.fromkeys(fileYearList))  #çoklayan kayıtları listeden siler
    fileYearList=list(set(fileYearList))  #çoklayan kayıtları listeden siler

    print(fileYearList)
    print(fileNameList)

    returnData=[fileYearList,fileNameList]
    print(returnData)
    return returnData

def createFolder(yearAndFileList): 
    i = 0
    dir=os.path.dirname(os.path.abspath(__file__)) + "/Test"
    
    for yearName in yearAndFileList:

        # define the name of the directory to be created
        path = dir+"/"+yearAndFileList[i]
        print(path)
        try:  
            os.mkdir(path)
        except OSError:  
            print ("Creation of the directory %s failed" % path)
        else:  
            print ("Successfully created the directory %s " % path)
        os.chdir(dir)
        i += 1

def MoveFiles(): 
    i = 0

    dir=os.path.dirname(os.path.abspath(__file__)) + "/Test"
    
    for filename in os.listdir(dir): 
        os.chdir(dir)
        shutil.move(filename, dir+"/2019")
        i += 1


if __name__ == '__main__': 

    x=yearAndFileList()
    y=x[0]
    print(y)
    
    #print(yearLists)

    createFolder(y)
    #MoveFiles()
    

    
