# write a recursive function to print all elements in a list
# hint : use list & index as parameters
fruits = ["Mango", 2 , "Banana" , 5.6, "Apple"]

def print_list(list,index=0):
    if (index == len(list)):
        return
    print(list[index])
    print_list(list,index+1)

print_list(fruits)