# nested dictionaries - jaise if-else statements ke time if ke andr bhi hum or if statemements likh skte
# vaise hi dictionary mein kisi bhi key ki value ko hum ek dictionary 
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
print(student)
print(student["Skills"]["Coding"])

