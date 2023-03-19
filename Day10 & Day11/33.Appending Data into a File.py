# Reading a file
fr = open("LogFile.txt","r")
data = fr.read()
print("Before Appending:")
print(data)
fr.close()

print("\n***************************")

# Appending data into a file
fw = open("LogFile.txt","a")
fw.write("Server-3\n")
fw.write("Server-4")
fw.close()

# Reading a file
fr = open("LogFile.txt","r")
data = fr.read()
print("After Appending:")
print(data)
fr.close()

print("\n***************************")