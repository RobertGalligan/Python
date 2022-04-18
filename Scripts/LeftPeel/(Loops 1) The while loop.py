# Looping is also called interation
# Warning be careful not to create an infinite loop
# Crtl + c will stop the program if you end up stuck in an infinite loop
count = 1

while count <= 5:
    print(count)
    count = count + 1

print("End of loop!")

count = 10

while count >= 0:
    print(count)
    count = count - 1

print("End of the world!")

count1 = 10
count2 = 100

while count2 >= 0 and count1 <= 40:
    print(count1, count2)
    count1 = count1 + 2
    count2 = count2 + 5

print("End of new loop")