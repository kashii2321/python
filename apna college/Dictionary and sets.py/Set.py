# Set - collection of unordered items
# jaise 11th mein maths mein sets tha vaise hi yha h 
# each element of a set must be unique and immutable
# set = {1,2,2,2} isme jaise 2 repeat hora h but vo ek hi baar store hoga to resolve hoke
# it will become set = {1,2}

# list , dictionary ko sets mein store nhi kr skte kyuki ye dono mutable hoti h baaki kr skte h

collection = {1, "Kashvi" , 21 , 1, "Yuvraj"}  # set ignores duplicate values
print(collection)
print(type(collection))
print(len(collection))    # length also ignores duplicate values

# null set bhi create kr skte h but uske liye we use set()
# kyuki ek dictionary ka bhi syntax is {} to python use as a dictionary treat krega
null_set = set()
print(null_set)
print(type(null_set))


