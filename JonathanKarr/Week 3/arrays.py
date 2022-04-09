import array    #array is a module you must import
numbers = array.array("i",[6,7,4,2])
#what makes an array different from a list is each variable must be the same type
# i = integer
for number in numbers:
    print(number)
print(numbers)