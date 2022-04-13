def squares(number):        # squares is the function and number is the parameters
    squared = []
    for i in range (len(number)):
        squared.append(number[i]**2)    #This will copy over each value i lands on in the squares list and copy it
                                        #into the squared list to the power of 2.
    return squared
print(squares([3,2,5,8]))

def squares_using_yield(number):        #yield is quicker to run, quicker to write and it also takes less space
    for i in range (len(number)):
        yield number[i]**2
print(list(squares_using_yield([3,2,5,8])))