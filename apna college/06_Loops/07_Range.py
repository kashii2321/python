# range - ek sequence of numbers return krta h and ye sequence start hota h 0 by default
# and increments by 1 by default 
# range(5) to hume return hoga 0,1,2,3,4
# step size mtlb ki kitne se hum increase krna chahte hai jaise usually hum 1 lete h += 1
# to 1 hi by default step size hota h

print(range(5)) 
# ab aise print kra to as such numbers print nhi hoge but if we want we can print the index
seq = range(5)
print(seq[0])
print(seq[1])
print(seq[2])
print(seq[3])
# isi sequence ke upr agr hume loop chalana h, we can write
for i in seq:
    print(i)   # isme humara ending number include nhi hota

# ab range ko likhne ke 3 ways hote h
# range(start?, stop, step?)
# start nhi specified to by default its 0
# step size nhi specified to by default its 1
# stop dena is compulsory

for i in range(10):
    print(i)   # range(stop), jb aise hota h to vo by default 10 ko stop value le lega 

for i in range(2,10):
    print(i)   # range(start,stop)

for i in range(2,10,2):
    print(i)   # range(start,stop,step)
    

