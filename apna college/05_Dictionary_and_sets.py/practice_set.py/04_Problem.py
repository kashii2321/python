# Figure out a way to store 9 & 9.0 as separate values in a set

# there are 2 ways to do this
# first is by storing one value as a string
Set1 = {9 , "9.0"}
print(Set1)

# other is by saving them in form of tuple with their data types
set2 = {
    ("int" , 9),
    ("float" , 9.0)    
}
print(set2)
