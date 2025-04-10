# Types of tokens 
# punctuators - symbols used for organising the program 
# () - parentthesis
# {} , [] , #, @ 
# python is implicit typed language where data has a type where we dont need to mention the data type unlike explicit languages like SQL, java

# Expression Execution
# string & numeric values can operate together using a *
a,b = 2,3
txt = "@"
print(2*txt*3) # since we are multiplying 2 and 3 with a txt then jo text h vo utni hi baar repeat hoga jaise 2*3 = 6 to @ ko hum 6 baar repeat hogi

#string and string operate together with a + also known as concatenation
a,b = "2",3
txt = "@"
print((a + txt)*b)

# numeric values can operate with all arithmetic values
e,f = 2,3
C = 4
print(e+f*C)

# Arithmetic expression with integer and float will result in float
k,y = 10,5.0
C = k*y
print(C)

# dividing two integers will also result in a float value
A,B = 10,5
C = A/B
print(C)

# integer divison i.e // of an integer and float will give float , integer divison is nothing but simple division by converting the answer as 
# an integer and rounding it off to the smaller integer value
G,H = 1.5,3
J = G//H
print(J)

# FLOOR - it gives the closest integer which is lesser than or equal to floor value
# (A//B) = floor(A/B)
T,S = 5,9
U = 5//9
print(U)

# REMAINDER (%) it is -ve if the denominator is -ve
A,B = -8,5
C = A%B
print(C)
