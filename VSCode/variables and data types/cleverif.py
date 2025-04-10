# Clever If statements
# <var> = (false_val, true_val) [<condition>]

Age = int(input("Age : "))
Vote = ("No", "Yes") [Age >= 18]
print(Vote)

Salary = float(input("Salary : "))
Tax = Salary*(0.1 , 0.2) [Salary >= 100000]
print(Tax)
