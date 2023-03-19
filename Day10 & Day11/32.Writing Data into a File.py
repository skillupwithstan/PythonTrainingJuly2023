# Reading a file
fr = open("LogFile.txt","r")
data = fr.read()
print("Before Writing:")
print(data)
fr.close()

print("\n***************************")

# Writing into a file
fw = open("LogFile.txt","w")
fw.write("Server-1\n")
fw.write("Server-2\n")
fw.close()

# Reading a file
fr = open("LogFile.txt","r")
data = fr.read()
print("After Writing:")
print(data)
fr.close()

print("\n***************************")

# Creating a file
fw = open("LogFile123.txt","w")
fw.write("Server-1\n")
fw.write("Server-2\n")
fw.close()

# Reading a file
fr = open("LogFile123.txt","r")
data = fr.read()
print("After Create & Write:")
print(data)
fr.close()

print("\n***************************")