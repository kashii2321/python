# write a program to accept marks of 6 students and display them in a stored manner
marks = []
m1 = int(input("Enter marks: "))
marks.append(m1)
m2 = int(input("Enter marks: "))
marks.append(m2)
m3 = int(input("Enter marks: "))
marks.append(m3)
m4 = int(input("Enter marks: "))
marks.append(m4)
m5 = int(input("Enter marks: "))
marks.append(m5)
m6 = int(input("Enter marks: "))
marks.append(m6)
marks.sort()
print(marks)

# we will use int(input()) coz the marks we added were in string data type so the sort 
# function will arrange it alphabetically like twenty one, thirty etc

# to select the same word in different lines and change them together, right click 
# -> change all occurences
