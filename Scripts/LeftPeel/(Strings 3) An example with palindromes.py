
# Palindrome is a sequence that is the same forward and backwards
# A palindrome is not the same as a mirror image

#
from tracemalloc import start


pal1 = "HousesuoH"
pal2 = "Applelppa"
pal2 = pal.lower()


start_index = 0
end_index = len(pal2) - 1

print(start_index, end_index)
# 0 8
print(pal2[start_index], pal2[end_index])
# a a

print("----------------------------------------")

start_index = 0
end_index = len(pal2) - 1

while start_index <= end_index:
    if pal2[start_index] != pal2[end_index]:
        break
    start_index += 1
    end_index -= 1

if start_index >= end_index:
    print("A palindrome appears!")
else:
    print("Not a palindrome!")
# A palindrome appears!

print("----------------------------------------")

