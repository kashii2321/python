# list is a inbuilt data type that stores a set of values
# it can values of different data types
# [] is used to make a list and can store upto any amount of values

fruits = ["Mango", 2 , "Banana" , 5.6, "Apple"]
print(fruits)
print(len(fruits))
print(type(fruits))
print(fruits[2])

# lists are mutable
print(fruits[2])
fruits[2] = "grapes"
print(fruits)

# in string, when we try to access the index that doesnt exist in it, it returns -1
# but is lists when we do so it returns error "list index out of range"
