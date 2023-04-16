'''
# Sample class with init method
class Person:
	# init method or constructor
	def __init__(self):
		self.name = "Arockia"
		
	# Sample Method
	def printname(self):
		print('Hello, my name is', self.name)
		
p = Person()
p.printname()

print("*****************************************")

class Addition:
	first = 0
	second = 0
	answer = 0

	# parameterized constructor
	def __init__(self, f, s):
		self.first = f
		self.second = s

	def display(self):
		print("First number = " + str(self.first))
		print("Second number = " + str(self.second))
		print("Addition of two numbers = " + str(self.answer))

	def calculate(self):
		self.answer = self.first + self.second

# creating object of the class
obj1 = Addition(10, 20)

# creating second object of same class
obj2 = Addition(40, 10)

# perform Addition on obj1
obj1.calculate()

# perform Addition on obj2
obj2.calculate()

# display result of obj1
obj1.display()

# display result of obj2
obj2.display()

print("*********************************************")
'''

class Person:
	# Constructor
	def __init__(self, name):
		self.name = name

	# To get name
	def getName(self):
		return self.name

	# To check if this person is employee
	def isEmployee(self):
		return False

# Inherited or Sub class
class Employee(Person):
	# Here we return true
	def isEmployee(self):
		return True

emp = Person("Arockia") # An Object of Person
print(emp.getName(),":", emp.isEmployee())

emp = Employee("Neo") # An Object of Employee
print(emp.getName(),":", emp.isEmployee())