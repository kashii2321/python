a = "this is a string"

# endswith
print(a.endswith("ng"))  # return true if the string ends with er, last ka part is substring se end hora h?

#capitalise 
print(a.capitalize())   # ye change already existing string mein change nhi krta rather ek nyi string bnake return deta h

# replace function, replace old occurences with new ones
print(a.replace("i" , "a"))

# find function , finds kya word humari string mein exist krta h ya ni if yes then it returns the index of the 1st occurence
print(a.find("i")) #if we try to find a value that doesnt exist in our string it will return -1 that means that it doesnt exist

# count function , count the no of times the substring exists in the string
print(a.count("i"))
