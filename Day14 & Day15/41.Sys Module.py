import sys

#print(sys.version)
#print(sys.path)
#print(sys.modules)

'''
for input in sys.stdin:
	if input.strip() == 'q':
		break
	print(f'Console Input : {input}')
print("Exit")

name = sys.stdin.readline()
sys.stdout.write(name)
#print(name)

age = input()
print(age)

sys.stderr.write("Error Occured!")

print("*******************************")
'''

# sys.exit()
servername = input("Enter the server name:")
if servername == "Server01":
	sys.exit("Invalid Server!")
	print("The entered value is:", servername)
else:
	print("The entered value is:",servername)
	print("To Be Continued..")
