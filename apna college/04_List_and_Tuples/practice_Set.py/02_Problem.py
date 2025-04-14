# write a program to check if a list contains a palindrome of elements 
List = [1,2,3,2,1]
copyList1 = List.copy()
copyList1.reverse()

if(copyList1 == List):
    print("yes")
else:
    print("no")

# we can also solve using this to make it more concise

if(List == List[::-1]):
    print("yes")
else:
    print("no")

    