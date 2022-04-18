# nested loops are when you take a conditional statement and place it inside
# another cconditional statement
# example
# if a < 5:
#     if b < 10:
#         print("Hi")

for i in range(0, 3):
    for j in range(0, 3):     #people will usually only use 3 per loop.
        print(i,j)           #You can keep nesting more and more but most

# 0 0
# 0 1
# 0 2
# 1 0
# 1 1
# 1 2
# 2 0
# 2 1
# 2 2

for i in range(0, 3):
    for j in range(0, 4):   
        print(i,j) 

# 0 0
# 0 1
# 0 2
# 0 3
# 1 0
# 1 1
# 1 2
# 1 3
# 2 0
# 2 1
# 2 2
# 2 3

for i in range(0, 7):
    for j in range(0,7):
        print(" ")          # If you don't put the , end function in it will print a
    print("0")              # new line each loop, which would output the below comment








# 0







# 0







# 0







# 0







# 0







# 0







# 0

for i in range(0, 7):
    for j in range(0, 7-i):
        print(" ", end="")         # This is how it should be
    print("0")  
#    0
#    0
#    0
#    0
#    0
#    0
#    0

for i in range(0, 7):
    for j in range(0, 7-i):
        print(" ", end="")         # This will create the left side of the pyramid
    print("0")  

#        0
#       0
#      0
#     0
#    0
#   0
#  0

for i in range(0, 7):
    for j in range(0, 7-i):
        print(" ", end="") 
    for k in range(0, i + 1):   # This will fill in the left side of the pyramid
        print("0", end="")
    print(" ") 

#        0
#       00
#      000
#     0000
#    00000
#   000000
#  0000000

for i in range(0, 7):
    for j in range(0, 7-i):
        print(" ", end="") 
    for k in range(0, 2*i+1):   # This will fill in the pyramid on both sides
        print("0", end="")          # Because if i is 0 then 0 * 2 is zero plus 1
    print(" ")                      # then 1 * 2 is 2 plus 1 is 3, so on and so forth

#        0
#       000
#      00000
#     0000000
#    000000000
#   00000000000
#  0000000000000

# This is cool because it all depends on i so if you change the value of i it will still work
# For example, you can make the code simple, functional and adjustable

pyramid_width = 15

for i in range(0, pyramid_width):
    for j in range(0, pyramid_width-i):
        print(" ", end="") 
    for k in range(0, 2*i+1):  
        print("0", end="")         
    print(" ")

#                0
#               000 
#              00000
#             0000000
#            000000000
#           00000000000
#          0000000000000
#         000000000000000
#        00000000000000000
#       0000000000000000000
#      000000000000000000000
#     00000000000000000000000
#    0000000000000000000000000
#   000000000000000000000000000
#  00000000000000000000000000000

pyramid_width = int(input('Enter number of rows required: '))

for i in range(pyramid_width,0,-1):
    for j in range(pyramid_width-i):
        print(' ', end='')          # printing space and staying in same line
    
    for j in range(2*i-1):
        print('0',end='')           # printing 0 and staying in same line
    print()                         # printing new line