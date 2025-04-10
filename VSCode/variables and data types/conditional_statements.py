# Syntax - IF, ELSEIF, ELSE
# if(condition) : 
#    statement 1                              gap of 4 spaces after : before writing the statement
# elif(condition) :
#    statement 2
# else :
#    statementN
# Python is an INDENTATION Language i.e we need to keep in mind the spaces we are giving
# Traffic light problem

Light = input("Light :")
if(Light == "Green"):
     print("Go")
elif(Light == "Red"):
     print("Stop")
elif(Light == "Yellow"):
     print("Wait")
else:
     print("Light is broken")

# nesting - if statement ke andr ek or if statement likhna
Age = int(input(" Enter the age : "))
if(Age >=18):
    if(Age >=80):
       print("Cannot drive")
    else:
        print("Can drive")
else:
    print("Cannot drive")