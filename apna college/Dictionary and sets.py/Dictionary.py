# dictionaries are used to store data in key:value form
# we store values in pairs
# for eg. Name = "Kashvi", idhr name key bnjaygi and Kashvi uski value
# i.e word is key and meaning is value
# can store any type of data, int , list, tuple, string, float, boolean

info = {
    "Name": "Kashvi",
    "Age": 21,
    "CGPA": 8.23,
    "Subjects" : ["accounts" , "IBM" , "project mgmt"],
    "Coding" : "Python",
}
print(info)
print(type(info))
print(info["CGPA"])
# keys can be of any data type int, string, boolean
# but not a list or dict
# for eg. [] cannot be a key, 2: can be a key
# dictionaries are mutable

info["Age"] = 20
print(info)
info["Surname"] = "Gupta"
print(info)
# they are unordered, koi fix rule nhi h ki konsi chiz pehle aaygi konsi baadme
# jaise strings, tuple mein index hote h vaise dictionary mein nhi hota
# they dont allow duplicate keys, ek naam ek hi key ka rhega vo dusri key ka nhi ho skta
# agr ek nyi value create krni chahe existing key ke saath to vo possible nhi
# vo existing value ko overwrite krdega

# null dictionary bhi create kr skte h 
null_dict = {}
print(null_dict)
# isme addition bhi kr skte
null_dict["Name"] = "Chokii"
print(null_dict)


