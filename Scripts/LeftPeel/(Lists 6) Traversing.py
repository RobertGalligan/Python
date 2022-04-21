# List is also known as an array (Java, C, C++...)
# Mutable means a list can change in length and type.
# Traverse means to go through the elements of an array

# Index   0   1   2   3   4   5   6   7   8   9  
ages =   [14, 15, 13, 18, 14, 15, 16, 18, 17, 15]    #<- Elements
weight = [45, 50, 43, 69, 56, 80, 75, 72, 62, 65]

# Traverse means to go through the elements of an array

for index in range(0, 10):      # This will go through the list index/element one at a time
    print(ages[index])          # This will print out what the element the index is on.

for index in range(0, len(ages)):   #Using the len(ages) will allow the number to be adjusted
    print(ages[index])              # If the list getsd long or shorter the program wont crash

for age in ages:                    # age becomes a variable
    print(age)


for index in range(0, len(ages)):      # This will go through the list index/element one at a time
    print(str(ages[index]) + " " + str(weight[index]))
# This will go the search each index up to the length of ages and for each
# one it will print out the index item of ages and weight

for index in range(0, len(ages)):      
    print("Person #" +  str(index) + ": " + str(ages[index]) + "\t" + str(weight[index]))
# str(index) prints out the index number relating to the search and corresponding output.

print("Person\t   age  weight")     # Reminder \t is equal to a tab movement
for index in range(0, len(ages)):      
    print("Person #" +  str(index) + ": " + str(ages[index]) + "\t" + str(weight[index]))
