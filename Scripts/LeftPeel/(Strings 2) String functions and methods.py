str1 = "Test String One"
str2 = "Test String Two"
str4 = "Test String\n More stuff\n I like mangos\n Yes!"

# Method is part of object-oriented programming and means we use the '.' operator

print(str1.count('e'))  # This will count how many time letter 'e' appears in the variable str1
# 2
print(str1.count('g'))
# 1
print(str1.count('ng'))
# 1
print(str1.count(' '))
# 2

# Count can be pretty useful when your doing data analysis
# or when you wanna see how many vowels are in a string...ect

print("-----------------------------------------")

# Find will search for thing you want and return the first ones place in the index

print(str1.find('e'))   
# 1
print(str1.find('S'))
# 5 
print(str1.find("String"))
# 5 -   Because "String" starts at index 5
print(str1.find("O"))
# 12

print("-----------------------------------------")

index = str1.find('e')
print(index)
# 1

print("-----------------------------------------")

# str1[index] = '3'
# line 36, in <module>    str1[index] = '3'
# TypeError: 'str' object does not support item assignment

# Which means that strings are like tuples, once you make a string you cant change it.
# You can reassign it but you cant change it.

# str1 = "Test String Blah!"     -   Reassigned

print("-----------------------------------------")

# Lets say you want to access just part of the string.
# This is called Splicing

print(str1[0:1])
# This will print a T
print(str1[0:5])
# This will print a Test
print(str1[3:8])
# This will print a t Str

str3 = str1[0:1] + '3' + str1[2:]
print(str3)
# T3st String One

print("-----------------------------------------")

print(str1.lower()) # will make letters lower case
print(str1.upper()) # will make letters upper case

# This will ignore numbers.

print("-----------------------------------------")

# Split is if you want to break down text into indivisual pieces

split_str1 = str1.split()
print(split_str1)
# ['Test', 'String', 'One']
# It will split by spaces, so if there is a blank space thats where it will seperate

split_str1 = str1.split('e')
print(split_str1)
# ['T', 'st String On', '']

split_str4 = str4.split('\n')
print(split_str4)
# ['Test String', ' More stuff', ' I like mangos', ' Yes!']