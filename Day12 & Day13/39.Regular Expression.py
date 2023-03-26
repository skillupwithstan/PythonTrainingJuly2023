import re

'''
userinput = input("Enter the text to search: ")
#print(re.search(userinput,"Neopolean"))
if(re.search(userinput,"Neopolean") != None):
    print("Text found")
else:
    print("Text is not found")

print("*****************************")

# r in front of the search pattern indicates 'raw string' where the special characters are treated as normal characters.
#keytext = "Neo\nKumar"
keytext = r"Neo\nKumar"
print(keytext)

#file_path = '\\sharepath\\data\\output.txt'
file_path = r'\\sharepath\\data\\output.txt'
print(file_path)

print("*****************************")

user_details = "User Account in AD is - Arockia"
print(user_details)
user_details_new = re.sub(r"Arockia",r"Neo",user_details)
#print(re.sub(r"Arockia",r"Neo",user_details))
print(user_details_new)
print(user_details)

if(re.search(r"N...o...n","Neopolean") != None):
    print("Pattern found")
else:
    print("Pattern not found")

if(re.search(r"N\d","N2O")!=None):
    print("Pattern found")
else:
    print("Pattern not found")

if(re.search(r"N\d*","N234O") != None):
    print("Pattern found")
else:
    print("Pattern not found")

if(re.search(r"N\d+","N2O") != None):
    print("Pattern found")
else:
    print("Pattern not found")

if(re.search(r"N\d?o","N2opolean") != None):
      print("Pattern found")
else:
      print("Pattern not found")

if(re.search(r"N\d{3}o","N224opolean") != None):
    print("Pattern found")
else:
    print("Pattern not found")

if(re.search(r"N[2-5]O","N3O") != None):
    print("Pattern found")
else:
    print("Pattern not found")

if(re.search(r"^Neo","Neopolean") != None):
    print("Pattern found")
else:
    print("Pattern not found")

if(re.search(r"n.$","Neopolean.") != None):
    print("Pattern found")
else:
    print("Pattern not found")

if(re.search(r"\w","Arockia123") != None):
    print("Pattern found")
else:
    print("Pattern not found")

if(re.search(r"Neo\s","Neopolean") != None):
    print("Pattern found")
else:
    print("Pattern not found")

if(re.search(r"Arockia|Neo","Neopolean") != None):
    print("Pattern found")
else:
    print("Pattern not found")
'''

print(re.search("N\d","['N1','N3','Neo']").group())
print(re.findall("N\d","['N1','N3','Neo']"))
pattern = re.compile("N\d")
print(re.findall(pattern,"['N1','N3','Neo']"))
