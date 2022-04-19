# List is also known as an array (Java, C, C++...)
# Mutable means a list can change in length and type.
# Immutable means the list stays the same length and type

#Index   0   1   2   3   4   5   6   7   8   9  
ages1 = [14, 15, 13, 18, 14, 15, 16, 18, 17, 15]    #<- Elements
ages2 = [15, 16, 17, 14]

# Access elements
# How to change elements
print(ages1[2])

ages1[2] = 15
print(ages1)

ages1[6] = "Rob"
print(ages1)

ages1[4] = True
print(ages1)

ages1[2] = 7.45
print(ages1)

# Concatenation aka Concat
# by using the (+ operator)

print(ages1 + ages2)

# or

ages3 = ages1 + ages2
print(ages3)

ages4 = ages1 + ages2 + ages1
print(ages4)

ages1 += ages2
print(ages1)

ages1 = [14, 15, 13, 18, 14, 15, 16, 18, 17, 15] 
ages2 = [15, 16, 17, 14]

ages2[0] = ages2[0] * 2         # Multiplies the first element by 2
ages2[1] = ages2[1] * 2         # Multiplies the second element by 2
print(ages2)

ages1 = [14, 15, 13, 18, 14, 15, 16, 18, 17, 15] 
ages2 = [15, 16, 17, 14]

ages3 = ages2 * 2       # If you multiply the entire list by 2 it will print out the list 2 times.
print(ages3)

ages1[1] = ages1[2] + ages1[3]  #here you are accessing an individual element
                                 #in the list so you can change its value.
print(ages1)

ages1 = ages1 + ages1            #here you are accessing an entire list
                                 #so it will just copy the lsit 2 times
    print(ages1)
#Copy a list onto itself or into a new list ( using the * operator )
# Access elements using (  [] -> ages1[1] ) 