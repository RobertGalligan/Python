# An if-statement is also known as a conditional statement or an if-then-else

a = 10
b = 20
c = 30

if a == b:
    print("Yes!")   # Nothing will print because a is not equal to b

if a <= b:
    print("Yes!")

string_of_names = "Raul, Quan, Timmy, Hiroki, Marie, Alfons, Tom, Emily, Kimmy"
timmy_age = 20

if "Timmy" in string_of_names and timmy_age < 15:
    print("Timmy is here")
if "Axel" not in string_of_names:
    print("Axel is not here")

if ("Timmy" in string_of_names) and (timmy_age < 15):   # parenthesis optional
    print("Timmy is here")
if "Axel" not in string_of_names:
    print("Axel is not here")

if ("Timmy" in string_of_names) and (timmy_age < 25):
    print("Timmy is here")
if "Axel" not in string_of_names:
    print("Axel is not here")

if ("Timmy" in string_of_names) and (timmy_age < 15) or ("Raul" in string_of_names): 
    print("Timmy is here")
if "Axel" not in string_of_names:
    print("Axel is not here")

#           False                       False                   True
if ("Tizzy" in string_of_names) and (timmy_age < 15) or ("Raul" in string_of_names): 
    print("Timmy is here")
if "Axel" not in string_of_names:
    print("Axel is not here")

#           False                       False                   False
if ("Tizzy" in string_of_names) and (timmy_age < 15) or ("Paul" in string_of_names): 
    print("Timmy is here")
    print("Yes, he is!")
if "Axel" not in string_of_names:
    print("Axel is not here")
 