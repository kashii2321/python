# dictionary methods
student = {
    "Name" : "Kashvi",
    "Age" : 21 ,
    "Skills" : {
        "Coding" : "Python" ,
        "DBMS" : "SQL" , 
        "MS" : "Excel"
     } ,
     "Gender" : "Female",
}

# mydict.keys() - returns all keys, saari saari ki keys ka collection hoke aajayga
print(student.keys())     # isme nested wali nhi aati sirf outerlayer wali aati h

# ab hum ise ek normal list ya tuple ke andr bhi convert kr skte h 
# uske liye hum type casting ko use krte h
print(list(student.keys()))

# to get total number of keys 
print(len(student))
print(len(list(student.keys())))

# mydict.values() - to return all the values in the dictionary
print(student.values())    # this can also be converted into a list
print(list(student.values()))

# mydict.items - returns all key,value pairs as tuple
print(student.items()) # this can also be type casted
print(list(student.items()))
# ab agr meko is tuple mein kisi ek pair ko access krna to vo bhi poss h
print(list(student.items())[2])

# mydict.get("key") - returns the key according to value 
# 2 methods h value return krwane ke ek simply dict["key"]
# and ek d.get("key") krke 
# ab difference dono mein ye h ki dict["key"] isme agr value exist nhi krti it will give error
# but d.get("key") mein none return hoke aayga

