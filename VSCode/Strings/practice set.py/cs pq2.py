# Write a program to find the greatest of 3 numbers entered by the user
a = int(input("Enter the number : "))
b = int(input("Enter the number : "))
c = int(input("Enter the number : "))
if(a >= b and a >= c):
    print("a is the greatest")
elif(b >= c):
    print("b is the greatest")
else:
    print("c is the greatest")