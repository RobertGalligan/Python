numbers = [3,4,7,11,3]
#          0 1 2 3 4 5
print(numbers)
print(numbers[1])
print(numbers[3])
print(numbers[-1])
numbers[1] = 2
print(numbers)
del numbers[1]
print(numbers)
numbers[1]=numbers[2]
print(numbers)
print(len(numbers))
numbers.append(17)
#add 17 to the end
print(numbers)
numbers.insert(2,5)
#This will insert a number in spot 2 and it will be a 5
print(numbers)
numbers.sort()
print(numbers)