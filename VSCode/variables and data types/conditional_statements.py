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

