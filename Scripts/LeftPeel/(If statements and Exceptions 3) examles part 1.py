# age = input("What is your age? ")
# Remember that inputs are always strings so we need to make it an integer again.
age = int(input("What is your age? "))
# age = int(age)

if age >= 0 and age < 21:
    print("Sorry, you're too young.")
elif age >= 21 and age < 65:
    print("Yup, you're good to go.")
elif age >= 65 and age < 125:
    print("Sorry, you're too old.")
else:
    print("Invalid age")

# this program is very easy to crash if the user does not enter an integer
# so you have to be careful of user input when making these programs

