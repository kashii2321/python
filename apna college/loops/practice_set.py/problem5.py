# search for a number x in tuple using loop 
# (1,4,9,16,25,36,49,64,81,100)

nums = (1,4,9,16,25,36,49,64,81,100)
X = int(input("Enter the number : "))
i = 1
while i < len(nums):
    if(nums[i] == X):
        print("Found at index" , i)
    i += 1