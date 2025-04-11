# loops - they are used to repeat instructions
# jaise spotify pr koi gaana sunte h to baar baar sunne ka option hota
# there are 2 types of loops - for loops and while loops

# while loops : 
# while loops mein jbtk condition jo likhi h vo true hoti h tbtk colon lgake jo bhi kaam h
# vo repeat hota rhega
# while True:
#     print("hello")  # true to hmesha true hi hota h to hello infinitely print hota rhega

count = 1
while count <= 5:
    print("hello")
    count += 1

print(count)

# ab jo humare variables hote h unhe hum iterator kehte h jaise upr eg mein count = 1 tha
# to count humara iterator h 
# and loop ek andr run krne ko hum iteration kehte h 
# usually hum loops ko chote variable se lete h jaise i,j,k

i = 1
while i<=100:
    print("Yes")
    i += 1

print(i)   

# print numbers from 1 to 5
i = 1
while i <=5:
    print(i)
    i += 1
print("loop ended")

# print numbers from 1 to 5 in reverse order
i = 5
while i>= 1:
    print(i)
    i -= 1
print("loop ended")

