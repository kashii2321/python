# slicing is accessing parts of String 
# string ko kaatna ya todna is known as slicing
# str[starting index : ending index]
# isme hmesha starting index is included but not ending Index 
# it means ki jo range di h humne vo wala part return hoke aajayga humare paas

str = ("apna college")
print(str[2:6])
print(str[2:])  #[2:len(str)]
print(str[:7])  #[0:7]


# negative index (only in slicing not while dealing with normal strings)
# string ke end se -1 se start hoke backwords index assign hota h
print(str[-8:-2])  #last wala print nhi hota i.e isme g return ni hoga

