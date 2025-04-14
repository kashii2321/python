# default parameters aisi value hoti h which are used when no argument is passed
# def calc_prod(a,b):
#     print(a*b)
#     return (a*b)

# calc_prod()
# ab jaise humne ye function bnaya and hum ise return krna chahte without passing any 
# arguments, to aise mein hum default parameters set krdege
def calc_prod(a=1,b=1):
    print(a*b)
    return (a*b)

calc_prod()
# ab humne isme a and b ki values define krdi to ab jb bhi call krege bina argument diye
# to by default vo a and b ki value 1 and 1 assume krlega

# hum isme single value bhi define kr skte but sirf b ki 
# a nhi define krege to chlega but agr a ko kra and b ko nhi to nhi chlega
# def calc_prod(a,b=1) - ye koi error nhi dega
# def calc_prod(a=1,b) - but ye error dega
# to agr hume default values deni h to hum last se shuru krege dena
