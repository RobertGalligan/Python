T = [[3-i for i in range (3)] for j in range (3)]
print(T)
s = 0
for i in range(3):
    s += T[i][i]
    print(s)