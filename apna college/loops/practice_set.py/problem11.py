# write a program to find the factorial of first n natural numbers using for loop
n = 5
factorial = 1
for i in range(1,n+1):
    factorial *= i
print("Factorial :", factorial)