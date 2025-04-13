# recursion - when a function calls itself repeatedly
# mtlb function khudko baar baar call krra, jaise
def show(n):
    print(n)

show(5)   
# ab agr main chahti ki jb main call kru ise to saath hi 4,3,2,1 bhi print hojaye 
# although we can use loops but hum ise recursion se krna chahte ho to?
def show(n):    # pehle kaam likhlo
    if(n==0):      # isko hum base case h jo decide krta h ki recursion ruk jaana chahiye ya nhi
        return    # jb hum return likhte h uska mtlb ye nhi ki value return krwa rha, mtlb ki simply bs return krre
    print(n)
    show(n-1)

show(5)
# isi function ko hum recursive function kehte h

# call stack - function ki calls ka stack 
# layers create hoti h hrr baar call krte h jb hum 
# agr hum base case nhi dege to recursion infinitely chlta rhega n ek point ke baad vo puri
# memory occupy krleta, jisse humara code crash ho skta h thats why base case is very important

# general cases mein hum loops hi use krte h, recursion special cases mein hi use krte h hum

# recursion through factorial
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * fact(n-1)

print(fact(5))
