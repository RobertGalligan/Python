# Tuple or Tuples
# Mutable (List) - That values can change
# Immutable (Tuple) - Values cannot change

# Lists by convention are the same type.    (By order!)
# With lists, if its a list of strings you can put them in alphabetical order,
# Tuples by conventions are/or can be different types.  (By structure!)
# Tuples could be structured by name age weight

# With lists, if its a list of strings you can put them in alphabetical order,
# if its a list of numbers you can put them in numberical order

# Lists take longer to create in memory and take up more memory
# a = ["Tim", 25, 185..........]
# list will store more memory aside expecting more data input to the list using the mutable ability 
# b = ("Lily", 21, 165.........)
# Tuples cant change so no extra RAM is required to store date since its immutable

# You can have a list of tuples.
# So you can organize a list of tubles using an element of the tuple

a = ["Tim", 25, 185]    # List
b = ("Lily", 21, 165)   # Tuple

print(a[0]) # we use [] for both so it doesnt become a function
print(b[0]) # a tuple accesses the elements in exactly the same way a list does

# Tim
# Lily

print("--------------------------------------------------")

for item in a:
    print(item)

# Tim
# 25
# 185

print("--------------------------------------------------")

for item in b:
    print(item)

# Lily
# 21
# 165

print("--------------------------------------------------")

a[0] = "Timothy"
print(a)

# ['Timothy', 25, 185]      # It changes element a in the list to Timothy

print("--------------------------------------------------")

# b[0] = "Liliana"
# print(b)

# line 41, in <module>
#     b[0] = "Liliana"
# TypeError: 'tuple' object does not support item assignment

# This goes to show that you can't change an item in a Tuple because they are immutable

print("--------------------------------------------------")

a.append(80)
print(a)

# ['Timothy', 25, 185, 80]  # We can append on a list

print("--------------------------------------------------")

# b.append(80)
# print(b)

# line 59, in <module>
#     b.append(80)
# AttributeError: 'tuple' object has no attribute 'append'

# This shows we can cannot append on to a tuple. Once a tuple is made its immutable.

print("--------------------------------------------------")

# If you do want to add onto a tuple, you have to make a whole new tuple.

c = (50) 
print(type(c))
# <class 'int'>

# You cant make a single element tuple.
# You need a comma to make a tuple.
c = (50,) 
print(type(c))

# <class 'tuple'>

print("--------------------------------------------------")

# b = ("Lily", 21, 165)   # Tuple
# c = (50,)

d = b + c
print(d)
print(type(d))

# ('Lily', 21, 165, 50)
# <class 'tuple'>

# This will allow you to add c onto b.
