# Dictionary with keys and values of different data types
numbers = {1: "One", 2: "Two", 3: "Three"}
print(numbers)
print(numbers[1])

numbers[4] = "Four"
print(numbers)

numbers[3] = "No-3"
print(numbers)

del numbers[3]
print(numbers)

#Loop
for key,value in numbers.items():
    print(key,":",value)

#To extract dictionary keys 
print(numbers.keys())

#To extract dictionary values
print(numbers.values())

#To extract both dictionary key and values
print(numbers.items())  #print(numbers)