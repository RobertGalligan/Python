# List is also known as an array (Java, C, C++...)
# Mutable means a list can change in length and type.
# Immutable means the list stays the same length and type

#Index   0   1   2   3   4   5   6   7   8   9  
ages = [14, 15, 13, 18, 14, 15, 16, 18, 17, 15]    #<- Elements
names = ["Ted", "Lily", "Ralph", "Amy"]
# len(), min(), max(), sum() and the operators 'in' and 'not in'

print(sum(ages))
# 155
# sum will add up all the elements and give you the total value.

# sum will only work with floats and integers

print( 14 in ages )
# will return True

print( 19 in ages )
# will retrun False

print( "Ted" in names )
# will return True

print( "Teddy" in names )
# will retrun False

for i in range(0, 10):
    print(i)

# This will search the range and then print each item in the range out.

print(5 in range(0, 10))
# Will print True
print(5 not in range(0, 10))
# Will print False

print(15 in range(0, 10))
# Will print out False
print(15 not in range(0, 10))
# Will print True