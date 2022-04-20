# List is also known as an array (Java, C, C++...)
# Mutable means a list can change in length and type.
# Immutable means the list stays the same length and type

#Index   0   1   2   3   4   5   6   7   8   9  
ages = [14, 15, 13, 18, 14, 15, 16, 18, 17, 15]    #<- Elements
names = ["Ted", "Lily", "Ralph", "Amy"]
names2 = ["Ted", "Lily", "Ralph", "amy"]    #since "amy" has a small 'a', Lily goes first
names3 = ["!Ted", "Lily", "Ralph", "amy"]
names4 = ["!Ted", "Lily", "Ralph", "9amy"]

# len(), min(), max(), sum() and the operators 'in' and 'not in'

print(len(ages))
print(min(ages))
print(max(ages))

print(len(names))
print(min(names))
print(max(names))

# ASCII values, Capital letters come before lower case
# Get an ASCII chart.

print(len(names2))
print(min(names2))
print(max(names2))

# '!' comes before capital letters, so !TED will be your new minimum

print(len(names3))
print(min(names3))
print(max(names3))

# '9' comes before symbols ( ! ) , so Ralph will be your new max

print(len(names4))
print(min(names4))
print(max(names4))