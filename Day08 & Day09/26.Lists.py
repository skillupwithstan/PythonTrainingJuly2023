# Create a empty List
sample_list = []
print(type(sample_list))

#Adding element into List
name_list = ["Arockia","Rajesh","Ravi"]
print(name_list[1])
print(len(name_list))

#Usage if None
print([None]*5)

#Accessing List element
name_list[1] = "Kumar"
print(name_list)

#Conditional Statement in Lists
list_of_network_devices = ["network1","network2","network3"]
network = "network2"
if network in list_of_network_devices:
    print(network + " is found")
else:
    print(network + " is not found")

#Looping in Lists
list_of_network_devices = ["network1","network2","network3"]

print("Iterating the list using range() method")
for index in range(0,len(list_of_network_devices)):
    print(list_of_network_devices[index])

print("Iterating the list using the keyword in")
for network in list_of_network_devices:
    print(network)

#Adding new element into the List
list_of_network_devices.append("network4")
print(list_of_network_devices)
