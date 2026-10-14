"""
number = int(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

"""


age = int(input("Enter your age: "))
if age >= 18 and age <= 50:
    print("You are eligible to ride.")
elif age < 18:
    print("You are not eligible to ride.")
else:
    print("You are old that you cannot ride.")
