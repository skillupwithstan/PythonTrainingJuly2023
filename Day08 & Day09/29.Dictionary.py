# Dictionary with keys and values of different data types
numbers = {1: "One", 2: "Two", 3: "Three"}
print(numbers)

# Access Dict. with keys
print(numbers[1])

# Add new key-value pair
numbers[4] = "Four"
print(numbers)

# Changing the value of key
numbers[3] = "No-3"
print(numbers)

# Deleting the key-value
del numbers[3]
print(numbers)

#Loop with dictionary keys & values 
for key,value in numbers.items():
    print(key,":",value)

#To extract dictionary keys 
print(numbers.keys())

#To extract dictionary values
print(numbers.values())

#To extract both dictionary key and values
print(numbers.items())  #print(numbers)
