# functions is a block of statements that perform a  specific task
# agr ek baar likhdia function ko to use kiti bhi baar use kr skte h jaise loop 

a = 5
b = 10
sum = a + b
print(sum)

# ab jaise iske baad or bhot saari lines of code h fir dobara sum krna h hume fir bhot saari lines of code h
# and aise baar baar repeat hora h , redundant h code to it reflects a bad coder
# isliye ki code baar baar repeat na ho we use functions jaise eg:

def Sum(a,b):       #isme def liya basically ki hum apne function ko define krre h
    sum = a + b     # to is pure code ko (line 13 to 16) ko kehte h "FUNCTION DEFINITION"
    print(sum)
    return sum

Sum(2,5)          # humne function bna dia to bs ab hume use call krna h arguments deke 

# def Sum(a,b):       ISKO HUM KEHTE H FUNCTION DEFINITION
    # sum = a + b     ISME A & B JO H UNHE HUM KEHTE H PARAMETERS
    # print(sum)
    # return sum
# Sum(2,5)            ISKO HUM KEHTE H FUNCTION CALL 
# ISME JO VALUES H UNHE WE CALL ARGUMENTS

def print_hello():
    print("hello")

print("hello")   # isko hum jitni baar likhege utni baar hello print hoke aayga
# to make a code less redundant we use functions

# ek aisa function bhi bna skte h jisme koi parameters na ho ya kch hume return nhi krwana ho
# jaise upr print("hello") isme koi parameters nhi h na ye koi input lera na koi return dera

output = print_hello
print(output)       # jo function output mein kch return nhi krta uske output mein none aajayga

