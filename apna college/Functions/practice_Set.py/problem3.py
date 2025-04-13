# write a function to print the elements of a list in a single line (list is the parameter)
food = ["Pasta", "Pizza", "Poha", "Panini"]
movies = ["Interstellar", "Top gun", "Hacksaw Ridge", "Shutter island"]
def print_el(list):
    for item in list:
        print(item, end =" ")
# pehle humne function ko define kra, uske andr argument pass kra, 
# uske baad proper indentation diya h, fir ek for loop lgaya properly iterate krne ke liye
# fir dobara indentation diya proper

print_el(food)
print_el(movies)

