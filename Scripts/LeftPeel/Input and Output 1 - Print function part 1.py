a = 42
b = 1.3
c = "Red"
d = 'Red'
e = True

print(a,b,c,d,e) # The commas will be output as spaces
# when adding a number with a str you must convert the number to a str or you will get an error
# print(str(a) + c + str(d)) - error
# concatentation is when you put two strings together into one
#       string   string
print( str(a)   +   d)

print( str(a) +  str(b))

print(c + " is my favorie colour")
print("Is it " + str(e) + "?")