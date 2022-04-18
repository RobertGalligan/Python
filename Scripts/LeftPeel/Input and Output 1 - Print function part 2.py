# print("He said, "It is the end of the world as we know it"")
# This will cause an invalid syntax error - which means you entered the code incorrect

# you can fix this by switching the first and last quotes to single quotes.
print('He said, "It is the end of the world as we know it"')

# another way to solve this issue is to use an escape (\)
# This will tell the code to ignore inside quotes so they do not get registered as being part 
# of the first quotes
print("He said, \"It is the end of the world as we know it\"")
print("He said, \'It is the end of the world as we know it\'")
print("He said, \'It\'s the end of the world as we know it\'")
print("He said, \"It\'s the end of the world as we know it\"")
print("She responds, \"You're an idiot. It\'s not the end of the world")

print("Ages:", end=" ")
print(34, end=" ")
print(14, end= " ")
print(19)

print("Ages:", end=" ")
print(34, end=":) :) ")
print(14, end= ":) :) ")
print(19)

print("Names: \nTim, \nQuan, \nMaria")  # \n - new line

print("Names: \rTim, \rQuan, \rMaria")  # \r - return line

print("Name Age Sex")
print("Tim 15 M")
print("Quan 18 M")
print("Maria 17 F")

print("Name \tAge \tSex")   # \t - is a tab ability that helps keep your code looking clean on the output
print("Tim \t15 \tM")
print("Quan \t18 \tM")
print("Maria \t17 \tF")

print("\t\t\n\r\t   Fred")