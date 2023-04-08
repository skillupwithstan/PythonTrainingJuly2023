'''

# Function declaration
def samplePrint():
    print("This is a sample function!")

samplePrint()

print("***************************")

# function with arguments
def add_numbers(num1, num2):
    sum = num1 + num2
    print('Sum: ',sum)

#add_numbers(4, 3)
add_numbers(num2 = 3,num1 = 4)
#add_numbers(num2 = int(input("Enter No-1:")),num1 = int(input("Enter No-2:")))

print("***************************")

def num_square_and_cube(type,num):
    if(type == "S"):
        result = num * num
        print('Square of 2 :',result)
    elif(type == "C"):
        result = num * num * num
        print('Cube of 2 :',result)
    else:
        print("Invalid Operation!")
    #return result

num_square_and_cube("S",2)
num_square_and_cube("C",2)
num_square_and_cube("A",2)


#print('Square of 2 :',num_square_and_cube("S",2))
#print('Cube of 2 :',num_square_and_cube("C",2))

print("***************************")

'''

# Reusability
def get_square(num):
    return num * num

for i in [1,2,3]:
    result = get_square(i)
    print('Square of',i, '=',result)

n = int(input("Enter the number:"))
print("Square until the given number:", n)
for j in range(1,n+1):
    result = get_square(j)
    print('Square of', j, '=', result)

print("***************************")