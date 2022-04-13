my_tuple_1 = (1,4,5)        #These are the two ways to write tuples - with brackets seperated by commas.
my_tuple_2 = 6,4,6,5,3      #Or just seperated by commas
print(my_tuple_1[1])        #this will print out 4
                            #Lists and tuples can both be indexed to access a certain elements 
                            # in the tuple or list and both starts at 0.
print(my_tuple_2)           ##This will print the tuple in parenthasis and thats how 
                            #we know its a tuple and not a list
print(len(my_tuple_2))      #This will give the length of the tuples which will be 5
print(10 in my_tuple_1)     #Using the "in" allows you to search for a certain thing in the tuple and get a true or false
print(5 not in my_tuple_1)  #not in will see if something is not in the tuple
my_tuple_1.append(8)        #This doesn't work since tuples are immutable. You cannot change the elements of a tuple 
                            #like you can with lists.
cordinates = (47,32)        #Since you cant change the values of a tuple you should use them for things that wont change.
red = (255,0,0)