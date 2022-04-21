# List is also known as an array (Java, C, C++...)
# Mutable means a list can change in length and type.
# 2D Lists in Python or Arrays in other languages
# Array(Java): 
    # All be the same type
    # Can't change length
# List(Python):
    # Any type you want
    # Length can change


# ages =   ["Hi", 14, 15, 13, 18, 14, 15, 16, 18, 17, 15] 
# Python lets you put strings and integers in your lists

# X O X    =  index 0
# X X O    =  index 1
# O O O    =  index 2

#              0   1   2
tictactoe = [['X','O','X']] # This is the 0 index
print(tictactoe)            # This will print the whole list
print("---------------------------------------------------------")
tictactoe = [['X','O','X']]
print(tictactoe[0][0])      # This will print the the first element from the first list
                            # First row = 'X' 'O' 'X'
                            # The first column will be 'X' 2nd = 'O' 3rd = 'X'
print("---------------------------------------------------------")
#              0   1   2      0    1    2      0    1    2
tictactoe = [['X','O','X'], ['X', 'X', 'O'], ['O', 'O', 'O']]   # we now have 3 columns
print(tictactoe[1][2])      # This will print from the 1 index so 'X' 'X' '0'
                            # and it will be element 2 which is 'O'

# This is a 3x3 list or array

for row in range(0, len(tictactoe)):
    for col in range(0, len(tictactoe)):
        print(tictactoe[row][col], end=" ")
    print("")

#This will print out the tictactoe board nicely spaced and positioned
# Lets say you want to add another row

# X O X    =  index 0
# X X O    =  index 1
# O O O    =  index 2
# O X X    =  index 3
print("---------------------------------------------------------")
tictactoe = [['X','O','X'],
             ['X','X','O'],
             ['O','O','O'],
             ['O','X','X']]

print(len(tictactoe))
for row in range(0, len(tictactoe)):
    for col in range(0, len(tictactoe[0])):
        print(tictactoe[row][col], end=" ")
    print("")
print("---------------------------------------------------------")

tictactoe = [['X','O','X'],
             ['X'],
             ['O','O'],
             ['O','X','X']]

# To fix this problem you column range to the length of the tictactoe row length

print(len(tictactoe))
for row in range(0, len(tictactoe)):
    for col in range(0, len(tictactoe[row])):
        print(tictactoe[row][col], end=" ")
    print("")
print("---------------------------------")    
print(tictactoe[1][0])      # This is how you can look at one specific value in the matrix
print(tictactoe[3][1])