# break

a = 0
while a < 5:
    print(a)
    if a == 2:
        break
    a += 1

print("---------")

#When the a reaches 2 the code will "break the loop" and move to the next part of code

for i in range(1, 20):
    print(i)
    if i % 7 == 0:  # This means when i gets to 7 if if % by 7 and ='s 0 so it breaks
        break

# continue

for i in range(1, 20):
    if i % 3 == 0:  # If i is devisable by 3 and equals 0 i  it will be skipped by the continue
        continue
    print(i)

for i in range(1, 20):
    if i % 2 == 0:  # If i is devisable by 2 and equals 0 i  it will be skipped by the continue
        continue
    print(i)

for i in range(1, 20):
    if i % 2 == 0 and i % 3 == 0:   #If i is devisable by 3 and 2 and equals 0 it will be skipped 
                                    #by the continue. 
        continue
    print(i)

for i in range(1, 20):
    if i % 2 == 0 or i % 3 == 0:  # If i is devisable by 3 or 2 and equals 0 i it will be skipped by the continue
        continue
    print(i)