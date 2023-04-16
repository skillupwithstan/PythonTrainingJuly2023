# Syntax Error
#if(a==10)

# Exceptions
#5 * (1/0)
#(total * 3)
#print(120 - input("Enter the utilized size:"))

print("********************************************")

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    #except ValueError:
    #    print("Oops!  That was no valid number.  Try again...")
    except Exception as e:
        print(e.args)    

print("The entered value is :", x)
print("**************************************************")

import sys
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
#        print(arg, 'has', len(f.readlines()), 'lines')
#        f.close()
    except OSError:
        print('Cannot open a file.', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
    finally:
        print("File Operation Completed!")   

print("**********************************************")

try:    
    raise Exception('server1', 'server2')
except Exception as inst:
    print(type(inst))    # the exception type
    print(inst.args)     # arguments stored in .args
    print(inst)          
    x, y = inst.args
    print('x =', x)
    print('y =', y)


print("*******************************************")

#raise NameError('Error Occured!')

def divide(x, y):
	result = x // y
	print("The division value is :", result)

divide(5, 2)
divide(5, 0)

def divide(x, y):
	try:
		result = x // y
		print("The division value is :", result)
	except ZeroDivisionError:
		print("Sorry! You are dividing by zero")

divide(5, 2)
divide(5, 0)

def divide(x, y):
	if(y != 0):
		result = x // y
		print("The division value is :", result)
	else:
		print("Sorry! You are dividing by zero")	

divide(5, 2)
divide(5, 0)

def divide(x, y):
	try:
		result = x // y
	except ZeroDivisionError:
		print("Sorry ! You are dividing by zero")
	else:
		print("The division value is :", result)
	finally:
		print('This is always executed!')

divide(5, 2)
divide(5, 0)

print("*********************************")

a = [1, 2, 3]
try:
	print ("Second element = %d" %(a[1]))
	print ("Fourth element = %d" %(a[3]))
except:
	print ("An error occurred")