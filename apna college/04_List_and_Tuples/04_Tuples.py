# inbuilt data type that helps us create a sequence of values
# they are immutable 
# can store values from different data types - strings, int, list
# () is used while making a tuple

tup = (1, 2 , "Kashvi" , [23], 5.9)
print(type(tup))

# indexing is allowed
print(tup[3])

# tuple doesnt support item assignment
# to create a single value tuple we need to add , after the element 
# eg . tup = (1,) 
# if we wrote tup(1) - it will give int data type
# we can also create empty tuple 
# eg. tup = ()

A = (1, 2, 3, 4)
print(type(A))
