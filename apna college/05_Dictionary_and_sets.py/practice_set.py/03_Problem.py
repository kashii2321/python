# write a program to enter marks of 3 subjects from the user and store them in a dictionary
# start with an empty dictionary & add one by one,
# use subject name as key and marks as value

Marks = {}
X = int(input("Enter Phy marks : "))
Marks.update({"Phy" : X })
Y = int(input("Enter Chem marks : "))
Marks.update({"Chem" : Y})
Z = int(input("Enter Bio marks : "))
Marks.update({"Bio" : Z})
print(Marks)