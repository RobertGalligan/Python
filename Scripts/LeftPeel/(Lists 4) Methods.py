# List is also known as an array (Java, C, C++...)
# Mutable means a list can change in length and type.
# Immutable means the list stays the same length and type
# ages.append()
# ages.insert(index, value)
# ages.extend([])
# ages.pop() or ages.pop(index)
# ages.remove(value)
# A list is an object.

#Index   0   1   2   3   4   5   6   7   8   9  
ages = [14, 15, 13, 18, 14, 15, 16, 18, 17, 15]    #<- Elements

# Object, Method()
ages.append(19)
ages.append(15)
print(ages)
# append will add a new element to the end of the list

#Index   0   1   2   3   4   5   6   7   8   9  10  11
ages = [14, 15, 13, 18, 14, 12, 15, 16, 18, 17, 15, 19]
#ages.insert(index, value)
ages.insert(5, 12)
ages.insert(5, 11)
ages.insert(5, 10)
print(ages)
# insert lets you select the exact spot you would likie to change in the list and with a new element.

# ages.extend([])
ages.extend([15, 16, 17, 18])
# ages = ages + [15, 16, 17, 18] same thing just less professional
print(ages)
# This allows you to extend the list by adding new values to the end of it.

#ages.pop() or ages.pop(index)
# ages = [14, 15, 13, 18, 14, 10, 11, 12, 12, 15, 16, 18, 17, 15, 19, 15, 16, 17, 18]
ages.pop()
print(ages)
# ages = [14, 15, 13, 18, 14, 10, 11, 12, 12, 15, 16, 18, 17, 15, 19, 15, 16, 17]
# 15 has "popped" off the end.

#Index     0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17
# ages = [14, 15, 13, 18, 14, 10, 11, 12, 12, 15, 16, 18, 17, 15, 19, 15, 16, 17]
ages.pop(3)
print(ages)
# This will remove the 3rd index
#Index     0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16 
# ages = [14, 15, 13, 14, 10, 11, 12, 12, 15, 16, 18, 17, 15, 19, 15, 16, 17]

# ages.remove(value)
# this will remove the chosen value from the list but only the first one.
ages.remove(13)
print(ages)
# ages = [14, 15, 14, 10, 11, 12, 12, 15, 16, 18, 17, 15, 19, 15, 16, 17]
# no more 13

ages.remove(15)
print(ages)
# ages = [14, 14, 10, 11, 12, 12, 15, 16, 18, 17, 15, 19, 15, 16, 17]
# only the first 15 was removed