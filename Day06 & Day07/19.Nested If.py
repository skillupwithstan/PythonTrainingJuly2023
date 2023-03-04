no1=int(input("Enter the value of no1:"))
no2=int(input("Enter the value of no2:"))
no3=int(input("Enter the value of no3:"))

if(no1 > no2):
    if(no1 > no3):
        print("The largest number is:",no1)
    else:
        print("The largest number is:",no3)
elif(no2 > no3):
    print("The largest number is:",no2)
else:
    print("The largest number is:",no3)

print("End of Script")