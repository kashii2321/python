# Types of operators
# jinpr operation perform hora we call them operands
# 1. Arithmetic operators generally used to perform mathematical functions
a = 5
b = 7
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) #remainder
print(a**b) #power, exponent

#2. Relational/Comparison operators    (==, !=, >, <, >=, <=)
# for equals ==
# for not equals !=
print(a == b) #false
print(a != b) #true

#3. Assignment Operators  (=, +=, -=, *=, /=, %=, **=)
num = 20
num += 30      #adds 30 in the num value assigned before
print(num)

# 4. Logical Operators (NOT, AND, OR) (they work on boolean values)
a = 70
b = 30
print(not (a>b))   #either true or false

# and operator - gives true only if both are true, agr ek bhi false h to it will give false
a = True
b = False
print("and operator : ", a and b)

# or operator - agr ek bhi value is true it will return true 
print("or operator : ", a==b or a>b)

