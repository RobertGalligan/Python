def sum (a,b):          #Function named sum
    return a + b        #After the return state everythying after doesnt matter
    print("This won't print")
print(sum(3,4))
def loop (num):
    for i in range(num):
        yield i     #If this was a return then it would return 0 because after the first return the loop would stop.
                    #Since it is a yield it will be a generator. and generators return generators not values
        print("test")
print(loop(3))
print(list(loop(3)))    #By using the list command you can see the values inside the function
count = loop(3)
print(next(count))      #This will count out the values in the function one at a time.  This will be 0
print(next(count))      #This will be 1
print(next(count))      #This will be 2
print(next(count))      #This last one will cause a spot interation error because there is nothing left to count in the list