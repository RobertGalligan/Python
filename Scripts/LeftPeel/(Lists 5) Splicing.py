# List is also known as an array (Java, C, C++...)
# Mutable means a list can change in length and type.
# Immutable means the list stays the same length and type

#Index   0   1   2   3   4   5   6   7   8   9  
ages = [14, 15, 13, 18, 14, 15, 16, 18, 17, 15]    #<- Elements

# Splicing - means to take a subsection of the list
print(ages[1:5])
# This will include everything from 1 up to 5 but not including 5
print(ages[1:9])
# This will include everything from 1 up to 9 but not including 9
print(ages[5:])
# This will incluide everything from 5 to the end
print(ages[:4])
# This will include everything from 0 up to 4 but not including 4
print(ages[:-1])
# This will everything from 0 up to 9 but not including 9
print(ages[:-8])
# This will everything from 0 up to 2 but not including 2
print(ages[-5])
# This will print the last 5th element of the list
print(ages[-5:])
# This will print the last 5 elements of the list

# [:-5] will print everything up to the last 5th element
# [-5:] will print from the last 5th element to the end of the list.




file_str = "Hi this is a string\n"
print(file_str[:-1])
print(file_str[0:2])
print(file_str)
# this is how it works with strings
