# create an empty set
empty_set = set() #{}
print(empty_set)
value_set = {34,64}
print(value_set)

# create a set of integer type
network_id = {120, 112, 114, 116, 118, 115}
print('Network ID:', network_id)

#Removed duplicates
network_id = {120, 112, 112, 118, 118, 115}
print('Network ID:', network_id)

print(max(network_id))
print(min(network_id))

# create a set of mixed data types
mixed_set = {'Storage', 101, -2, 'Database'}
print('Set of mixed data types:', mixed_set)
network_id = {120, 112, 114, 116, 118, 115}
mixed_set.add("Arockia")
mixed_set.update(network_id)
print("After Merging: ",mixed_set)
mixed_set.remove(-2)
print("After removal of -2: ",mixed_set)
print(len(mixed_set))

#Set Operations
set_A = {100,102,104,106,108,110}
set_B = {98,95,100,101,105,107,108}
print("SET - A: ",set_A)
print("SET - B: ",set_B)
print(set_A & set_B)
print(set_A - set_B)
print(set_A | set_B)