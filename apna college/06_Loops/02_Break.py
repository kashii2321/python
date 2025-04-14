# BREAK 
# Break - used to terminate the loop when encountered, hum jha bhi break likhdege loop vha ruk jayga
i = 1
while i <= 5:
    print(i)
    if(i == 3):
        break
    i += 1

print("end of loop")   # 5 tk numbers kbhi print hi ni hoge kyuki humne loop ko break krdia

nums = (1,4,9,16,25,36,49,64,81,100)
X = 64
i = 1
while i < len(nums):
    if(nums[i] == X):
        print("Found at index" , i)
        break
    else:
        print("finding...")
    i += 1
print("end of loop")
