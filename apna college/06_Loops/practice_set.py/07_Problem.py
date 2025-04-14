# search for a number X in the tuple using for loop
# (1,4,9,16,25,36,49,64,81,100)
nums = (1,4,9,16,25,36,49,64,81,64,100)
X = 64
idx = 0
for el in nums:
    if(el == X):
      print("Number found idx" , idx)
    idx += 1    # humare paas idhr dono index aayge jha vo value h
    # agr hum chahte h ki first occurence ke baad rukjaye we can use break

# this is called linear search in programming which means ki ek line ke andr search