# sbse easy function jo hum ek file pr perform krte h vo ye h ki humne ek file ko open kra
# jaise real life mein hum apni koi file ko leke aate h use kholte h pdhte h uske andr ka
# and then bnd krke rkhdete h
# to open a file, we have an in built function in python

# open = ("file name","mode")
# mode ka mtlb hota h kya format hota h file I/O ka ki hum read krne wale h ya write 
# ya kch bhi, we need to tell it before, if not stated python assumes that we will read it
# so if we open it in a read mode but we are trying to write in it, it will show error

F = open("demo.txt","r")
# agr yhi pr vo file nhi h khi or saved h to hume uska pura path likhna pdhta h
Data = F.read()
print(Data)
print(type(Data))
F.close()
# with open("demo.txt","r") as file:
#     data = file.read()
#     print(data)

# r - open
# w - write and truncate
# x - create a new file and open it for writing
# b - binary mode
# t - text mode
# + - open a desk file for updating(Reading and writing)
# a - open for writing, appending to the end of the file if it exists
