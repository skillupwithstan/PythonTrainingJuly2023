#Escaping Characters

out = "This is a \"Test Server\"."
print(out) # This is a "Test Server".

######################################################

#Slicing String
str1 = 'yellow flat'
print(str1[1])     # => 'e'
print(str1[-1])    # => 'w'
print(str1[0:6])   # => 'ow'
print(str1[:4])    # => 'yell'
print(str1[-3:])   # => 'low'
print(str1[:-3])

######################################################

#Get Length Of a String
#Example - 1
servername = input("Enter the server name:")
print(servername)
print(len(servername))

#Example - 2
colors = ["red", "yellow", "green"]
print(colors)
print(type(colors))
print(len(colors)) # 3

######################################################

#String Concatenation
firstname = input("Enter the First Name:")
lastname = input("Enter the Last Name:")
print("User Name:", firstname + "-" + lastname)

######################################################

#Sring Formatting
#Example - 1
msg1 = 'Running {} out of {} servers.'
print(msg1.format(3, 10)) # Running 3 out of 10 servers.

#Example - 2
msg2 = 'Server Name: {name} ; IP Address: {ip} ; Port: {port}.'
print(msg2.format(name='localhost', ip='53.23.12.4', port='443'))

######################################################

#Lower Case & Upper case change
greetings = "Welcome To Python"
print(greetings.lower())
print(greetings.upper())

######################################################

#Strip - Remove unwanted spaces/characters
text1 = '   apples and oranges   '
print(text1.strip())       # => 'apples and oranges'

text2 = '...+...apples and oranges...-...'
# Here we strip just the "." characters
print(text2.strip('.')) 

# Here we strip both "." and "+" characters
print(text2.strip('.+'))

# Here we strip ".", "+", and "-" characters
print(text2.strip('.+-'))

######################################################

#Change Title 
heading = "dark knight"
print(heading.title())

######################################################

#Splitting the String - Sub String
text = "Red Apple"
print(text)
print(type(text))
print(text.split())  # print(text.split(" "))    
print(text.split()[0] + "\n" + text.split()[1])
print(type(text.split())) # Prints: ['Red', 'Apple']
print(text.split('l'))

######################################################

#Find first occurance of a character index in a string
mountain_name = "Mount Everest"
print(mountain_name.find('Good'))

#if(mountain_name.find('Good') > -1):
#    print("This key word is not found")

######################################################

#Replace a character/string
fruit = "Apple"
print(fruit.replace('Apple', 'Mango'))
print(fruit)

######################################################

#Join multiple Strings - concatenates a list of strings together.

x = " ".join(["This", "is", "Awesome"])  #"This" + " " + "is" + " " + "Awesome"
print(x)

######################################################
