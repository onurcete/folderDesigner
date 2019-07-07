# import the os module
import os

# detect the current working directory and print it
path = os.getcwd()  
print ("The current working directory is {0}".format(path)) 

# detect the file exist
a=os.path.isfile('./deneme.txt') 
print(a)

# detect the directory exist
a=os.path.isdir('./Doküman') 
print(a)

# detect the directory or file exist
a=os.path.exists('./xx.txt')
print(a)


# define the name of the directory to be created
path = "/Users/onur.cete/Desktop/python/yearonur"
try:  
    os.mkdir(path)
except OSError:  
    print ("Creation of the directory %s failed" % path)
else:  
    print ("Successfully created the directory %s " % path)


# define the name of the directory to be created
path = "/Users/onur.cete/Desktop/python/yearonur/1/2"

try:  
    os.makedirs(path)
except OSError:  
    print ("Creation of the directory %s failed" % path)
else:  
    print ("Successfully created the directory %s" % path)


# define the name of the directory to be deleted
path = "/Users/onur.cete/Desktop/python/yearonur/1/2"

try:  
    os.rmdir(path)
except OSError:  
    print ("Deletion of the directory %s failed" % path)
else:  
    print ("Successfully deleted the directory %s" % path)