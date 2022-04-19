# List is also known as an array (Java, C, C++...)
# Lists in python are much more flexible than in many other languages

# Ages: 14, 15, 17, 18, 14, 15, 16, 18, 17, 15

#Index  0   1   2      3     4  5   6     7   8   9  
ages = [14, 15, 17, "Name", 14, 15, 16, True, 17, 15]   # Square brackets make a list with elements
# ages = list[14, 15, 17, "Name", 14, 15, 16, True, 17, 15] # This is another way to make a list
print(type(ages))  #This will "access" index 4 which is element 14
print(type(ages[4]))
print(type(ages[3]))
print(type(ages[7]))

# for i in range(0,10):
# Computer memory (RAM)
# Ages starts at some place
# 0 -> 14
# 1 -> 15
# 2 -> 17
# 3 -> "Name"