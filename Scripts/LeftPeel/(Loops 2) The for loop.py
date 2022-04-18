count = 0
while count < 5:                # Not really designed for counting
    print(count)
    count = count + 1

for count in range(0, 5):       #Designed for a specific amount of information
    print(count)                #This will print of everytyhing in the range (0, 5)
                                #(0, 1, 2, 3, 4)

for count in range(0, 5): 
    if(count < 2):      
        print(count)            #This will print out 0, 1 because they qare less then 2
    else:
        print("Bubbles")        #This will print out bubbles for 2,3, and 4

# print(10 % 3) will give you the remainer of 1

for i in range(0, 50): 
    if i % 3 == 0:
        print(i)

for i in range(0, 50): 
    if i % 10 == 0:
        print(i)

for i in range(15, 50): 
    if i % 2 == 0:
        print(i)

# Ctrl + / will take a highlighted section of code and comment it out 