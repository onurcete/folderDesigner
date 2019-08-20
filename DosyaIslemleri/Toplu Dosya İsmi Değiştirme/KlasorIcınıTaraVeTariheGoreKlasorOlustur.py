import os,time
import shutil
from datetime import datetime

dir=os.path.dirname(os.path.abspath(__file__)) + "/Test/" #.py nin çalıştığı dizini gösterir
#print('Dizin Giriniz:')
#dir = input()
#dir = dir +"/"

def fileInfo(): 
    i = 0
    fileYearList=[]
    fileNameList=[]
    fileMonthList=[]
    fileYearMonthList=[]
    filesInfo=[]

    dummy=[]
    
    #os.getcwd() # working directory gösterir
    
    for filename in os.listdir(dir): 
        os.chdir(dir)
                
        if os.path.isfile(filename): 
            fileYearList.append(datetime.fromtimestamp(os.path.getmtime(filename)).strftime('%Y'))
            fileMonthList.append(datetime.fromtimestamp(os.path.getmtime(filename)).strftime('%m'))
            fileYearMonthList.append([datetime.fromtimestamp(os.path.getmtime(filename)).strftime('%Y'),
                                      datetime.fromtimestamp(os.path.getmtime(filename)).strftime('%m')])
            fileNameList.append(filename)
            filesInfo.append([datetime.fromtimestamp(os.path.getmtime(filename)).strftime('%Y'),
                          datetime.fromtimestamp(os.path.getmtime(filename)).strftime('%m'),
                          filename])
        

    fileYearList=list(set(fileYearList))  #çoklayan kayıtları listeden siler
    fileMonthList=list(set(fileMonthList)) #çoklayan kayıtları listeden siler

    #print(fileYearList)
    #print(fileNameList)

    #uniq = []
    #[uniq.append(x) for x in fileYearMonthList if x not in uniq]
    #print(uniq)
    fileYearMonthList_ = []
    for l in fileYearMonthList:
        if l not in fileYearMonthList_:
            fileYearMonthList_.append(l)

    returnData=[fileYearList,fileMonthList,fileNameList,fileYearMonthList_]
    #print(returnData)
    #print(filesInfo)
    return [returnData,filesInfo]

def createFolder(fileGroups): 
    i = 0
    
    for yearMonthName in fileGroups:

        # define the name of the directory to be created
        #print(yearMonthName)
        if yearMonthName[0] not in os.listdir(dir):
            yearPath = dir+"/"+yearMonthName[0]
            os.mkdir(yearPath)
            monthPath= dir+"/"+yearMonthName[0]+"/"+yearMonthName[1]
            os.mkdir(monthPath)
        elif yearMonthName[0]  in os.listdir(dir):
            if yearMonthName[1] not in os.listdir(dir+"/"+yearMonthName[0]):
                monthPath= dir+"/"+yearMonthName[0]+"/"+yearMonthName[1]
                os.mkdir(monthPath)
        
        #os.mkdir(path)
        #try:  
        #    os.mkdir(yearPath)
        #    os.mkdir(yearPath+"/"+fileGroups[i][1])
        #except OSError:  
        #    print ("Creation of the directory %s failed" % yearPath)
        #else:  
        #    print ("Successfully created the directory %s " % yearPath)
            #os.chdir(dir)
        i += 1

def MoveFiles(fileGroups): 

    i = 0
    for filename in fileGroups: 
        #os.chdir(dir)
        if filename[2] in os.listdir(dir):
            try:
                #print(filename)
                #print(filename[2], dir+"/"+filename[0]+"/"+filename[1])
                shutil.move(filename[2], dir+"/"+filename[0]+"/"+filename[1])
            except OSError:
                print("Moving file has error")
        i += 1


if __name__ == '__main__': 

    x=fileInfo()
    #print(x)
    fileYearNames,fileMonthNames,fileNames,fileGroups,fileYearMonths=x[0][0],x[0][1],x[0][2],x[1][:],x[0][3]
    print("File Year Names:",fileYearNames)
    print("File Month Names:",fileMonthNames)
    print("File Names:",fileNames)
    print("File Group:",fileGroups)
    print("File Year and Months:",fileYearMonths)
    

    createFolder(fileGroups)
    MoveFiles(fileGroups)