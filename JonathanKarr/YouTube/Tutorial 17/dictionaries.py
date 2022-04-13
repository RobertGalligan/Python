phone_numbers = {"doctor":1234567890,"electrician":8000000011}  #This is one way to make a dictionary 
                                                                #using the curly braces and then making your 
                                                                #key in brackets then semicolon followed by your value
grades = dict(homework = 97, tests = 94, exam = 100)            #This is the second way using dict.then open and closed
                                                                #parethases then your key with an = then your value and then 
                                                                #seperate with a comma for any addional keyss
print(phone_numbers)
print(grades)
print(phone_numbers["doctor"])
print(phone_numbers.get("Mom","This value doesn't exist"))      #Mom is not in the dictionary but if you use the .get command
                                                                #it will continue to run and Say this value doesnt exist
for key in phone_numbers.keys():
    print(key, "->", phone_numbers[key])    #This will print out all the keys values pairs The arrow is needed
phone_numbers ["doctor"] = 8880000088       #This changes the doctors phone number value
print(phone_numbers)
phone_numbers ["author"] = 4567890123       #This will add author and his number
print(phone_numbers)
del phone_numbers["author"]                 #This will delete the author from the dictionary
print(phone_numbers)
print(len(phone_numbers))                    #This will the length of the phonenumbers dictionary
del phone_numbers
print(phone_numbers)