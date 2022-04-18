# age = input("What is your age? ")
# print(type(age))

# try-catch (Java) or in Python try-except
try:
    age = int(input("What is your age? "))  # if they ente3r a none integer value it will
                                            #create a ValueTypeError
    if age < 21:
        print("You're way too young.")

except ValueError:
    print("ValueError please type a number.")  
#If the user enters a not integer number such as "sadfjhb" it 
#will return ValueError.

except:
    print("Another error")
