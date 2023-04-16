def cube(num):
	return num*num*num

#print("Normal function ==> cube:", cube(2))

#lambda_cube = lambda num: (num*num*num)
#print("Lambda function ==> cube:", lambda_cube(2))

Max = lambda a, b : a if(a > b) else b
#print(Max(12, 2))

numbers = [50, 35, 22, 87, 54, 62, 17, 25, 73, 60]
dividebytwo = list(filter(lambda x: (x % 2 == 0), numbers))
print(dividebytwo)