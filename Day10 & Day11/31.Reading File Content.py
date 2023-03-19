# Reading entire file content
filedata = open("FileContent.txt")

#print(filedata)
#Option - 1
#content = filedata.read()
print(filedata.read(15))
#print(content)
#print(content.split()[0:3])

#for i in (content.split()[0:3]):
#    print(i,end="\n")

#Option - 2
filedata = open("D:\Python Course\sample.txt")
#print(filedata.readlines())
for f in filedata.readlines():
    print(f,end="")

filedata.close()

print("\n***************************")

# Reading the content line by line

filedata = open("FileContent.txt","r")
line1 = filedata.readline()    
print(line1,end="")
line2 = filedata.readline()    
print(line2,end="")
line3 = filedata.readline()    
print(line3,end="")
filedata.close()

print("\n****************************")

#Reading the contents of a file into a list

filedata = open("FileContent.txt","r")
list_var = filedata.readlines()
print(type(list_var))
for line in list_var:
    print(line,end="") 
filedata.close()

print("\n***************************")

# Reading the contents of a file into a string

fldata = open("FileContent.txt","r")
data = fldata.read(8)
print(data)
print(type(data))
fldata.close()

print("\n***************************")

# Iterating a file

fldata = open("FileContent.txt","r")
for line in fldata:
    #if(line != "Server-3"):
    if(line.replace("\n","") != "Server-3"):
        print(line,end="")
fldata.close()