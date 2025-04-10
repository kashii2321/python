#Arithmetic Operators
#eg: + , - , / , * 

a = 5
b = 9 
c = a + b
print(c)

#Assignment Operators
#eg: = , += , -=

a = 3-2
print(a)
b = 9
b += 3 #increment the value by 3 and then assign it to b 
print(b)

#Comparison Operators (result always in boolean)
#eg: == , > , < , >= , != (not equal to)

d = 5>=5
print(d)

#Logical Operators
#eg: AND , OR , NOT

e = True or False

#Truth table of 'or'
print("True or False is", True or False)
print("True or True is", True or True)
print("False or True is", False or True)
print("False or False is", False or False)

#Truth table of 'and'
print("True and False is", True and False)
print("True and True is", True and True)
print("False and True is", False and True)
print("False and False is", False and False)

print(not(True))