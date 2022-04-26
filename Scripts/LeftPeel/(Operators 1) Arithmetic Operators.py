a = 10
b = 5
c = 1
d = -1

print(a + b)
print(a * b - c)
print(a * (d + a) - b)
print(a / (b * c -a))
print(a / (b * (c -a * (d / d * c + (a * a)))))
# EOF means End Of File
# Parcing means its trying to take the code apart and run it for you.
# SyntaxError means you made a mistake when typing
print(a / (b * (c -a * (d / d * c + (a * a)))))   #remove one bracket to see error

print(a ** b)                # Same thing
print(pow(a, b))

print(a ** b ** d)           # Same thing
print(pow(a, pow(b, d)))

print(10 // 3)      # This tells you how many times the number goes into the number
print(int(10 / 3))  # This is a different way to do the same thing
print(20 // 3)
print(int(20 / 3))
print(30 // 3)
print(int(30 / 3))

print(10 % 3)       # This is called the modulus operator
print(20 % 3)       # It gives you the r4emaining number that was not able to be divided
print(30 % 3) 