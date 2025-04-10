# there are two types of conversion in python 
# 1. type conversion - automatically 
# 2. type casting   - zabardasti
# jb ek type ke variable ko dusre type ek variable mein convert krna

a = 2
b = 4.2
sum = a + b  # ab ek int h n ek float to python automatically int ko float mein convert krdega since float is superior to int this is type conversion
print(sum)   # 2.0 + 4.25 = 6.2

a = "2"
b = 4.25
c = int(a)  # this is called type casting ki hume batana pdra h python ko data type convert krne ke liye vo automatically nhi krra
print(b+c)
