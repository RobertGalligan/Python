file_handle = open('text.txt', 'r') # open is what will get the file, the first variable is the name of the file, and the second one is the 
                                    # mode in how you want to access the file. 'r' means read        

# t = file_handle.read(4) # This will print out the first for characters of the file
# print(t)
# noun

# t = file_handle.read(4) # Doing it again will print off the next 4
# print(t)
# : st

# s = file_handle.readline()
# print(s.strip())    # will remove what ever you want from the end but \n is the default

s = file_handle.readline().strip()  # Strip can also be used in this spot too
print(s)

for line in file_handle:    # This will print all the filke out
    print(line.strip())

file_handle.close() 
# make sure to close out of the file or it can lead to memory leaks
# or leave your program hanging

print("-----------------------------------------------------------------------")

with open('text.txt', 'r') as file_handle:
    lines = file_handle.readlines() # readlines give you a list.
    print(lines)

print("-----------------------------------------------------------------------")

with open('text.txt', 'r') as file_handle:
    lines2 = file_handle.readlines() # readlines give you a list.
    for line in lines:
        print(line.strip()) # now its a print out and not a list

print("-----------------------------------------------------------------------")

with open('text.txt', 'r') as file_handle:
    for line in file_handle.readlines():
        print(line.strip()) 