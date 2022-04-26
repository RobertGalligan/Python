# List is also known as an array (Java, C, C++...)
# List comprehension

from hashlib import new


print("--------------------------------" )

threes = []
for i in range(1,20):   #this i will go in every spot from 0-20 but not 20
    if i % 3 == 0:      #this mean for every spot the one above is on, if that number divided by 3
                        #the that will be appended into the threes list.
        threes.append(i)
print(threes)
# [3, 6, 9, 12, 15, 18]

fours = [i for i in range(1, 20)]   # This will put the "i / index" into the other i for each index
                                    # Which then becomes the four list.
print(fours)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

three = [i for i in range(1, 20) if i % 3 == 0 ]   # now we combine them.
    # This will put the "i / index" into the other i for each index and check if it is divisable by 3.
print(three)
# [3, 6, 9, 12, 15, 18]

print("--------------------------------" )

powers = [pow(i, i) for i in range(1,10)]   #This will take i and times it to 
                                            #the power of i, for i in range(1, 10)
print(powers)

powers1 = [i**i for i in range(1,10)]   #This is the same thing but its using "*" instead of pow 
print(powers1)

powers2 = [2**i for i in range(1,10)]   #this way you get 2 to the power of i for i in range(1, 10)
print(powers2)

powers3 = [2**i for i in range(1,10) if 2**i % 8 == 0]   
print(powers3)
# this will be 2 to the power of i for i in range 1 - 10 if the 2 to the power of i divided by 8 leaves 
# nothing behind or equals 0

# using list comprehension will lets you sort things out like all odd or all even, maybe
# you want multiples of something. You can also loop over things and make a new list.

print("--------------------------------" )

names = ["Ted", "Ray", "Bill", "Mary", "Madeline",
        "Gertrude", "Quan", "Masahiko", "Lily", "Aaron"]
new_name_list = [name for name in names if len(name) < 5]
print(new_name_list)
# This means it will search through the index of names and for the name in the names list if it is
# less then 5 letters it will be added to the new list.

print("--------------------------------" )
