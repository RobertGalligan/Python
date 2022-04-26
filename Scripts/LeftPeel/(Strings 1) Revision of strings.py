
str1 = "Test\t String\t One"
str2 = "Test\n String\n Two"
lst1 = [4, 5, 6]
print(str1)
print(str2)
# Test     String  One
# Test
#  String
#  Two
print(str2[0])
print(str2[1])
print(str2[2])
print(str2[3])
print(str2[4])
# T
# e
# s
# t
#
for char in str2:
    print(char)

for i in range(0, len(str2)):
    print(str2[i])

# T
# e
# s
# t


# T
# e
# s
# t


 
# S
# t
# r
# i
# n
# g



# T
# w
# o

print("--------------------------------------")

# in or not in

print(4 in lst1)
print('Test' in str1)
print('Test\t 5' in str1)
print('Test\t 5' not in str1)
# True
# True
# False
# True

# String manipulation