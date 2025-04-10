# single line if statements also known as ternary operator
# <var> = <val1> if <condition> else <val2>

Food = input("Food : ")
Eat = "Yes" if Food == "cake" else "No"
print(Eat)

Food = input("Food : ")
print("Sweet") if Food == "cake" or Food == "Jalebi" else print("Not sweet")