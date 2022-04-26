# Boolean Operators (aka Logical Operators)
# By holding down controil and using the 
# left or right arrow it will skip to the next white space...blank space.
# and, or, not

# and operator - If all statements are True then the answer is True, if one is not then it is false

#      True     True
print(1 > 0 and 4 < 7)
#      True     False
print(1 > 0 and 4 > 7)
#      True     False      True
print(1 > 0 and 4 > 7 and 2 == 2)

# or operator - If one statement is True then you will get True 

#      True     True
print(1 > 0 or 4 < 7)
#      True     False
print(1 > 0 or 4 > 7)
#      False     False
print(1 < 0 or 4 > 7)
#      True     False      True
print(1 > 0 or 4 > 7 or 2 == 2)

# not operator - If something is True it makes it False, and if its False it makes it True

print(1 > 0)
print(not 1 > 0)
print(not 1 > 10)

#      True     True      True
print(1 > 0 and 2 < 3 or 4 > 1)

#      True     True      False
print(1 > 0 and 2 < 3 or 4 > 10)

#      True     False     True
print(1 > 0 and 2 < 1 or 4 > 1)

#      True     False      False
print(1 > 0 and 2 < 1 or 4 > 10)

#         False     True     False
print(not 1 > 0 and 2 < 3 or 4 > 10)
