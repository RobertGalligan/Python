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
    if i % 7 == 0:
        break
    