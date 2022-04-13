def add (a,b):
    c = a + b
    return c
a = 77      #this a will not affect the a in the def function add befcause it is outside of the function
print(add(1,2))
# print(c) doesn't work because of scope, it is inside the function so this has not been defined outside the function
def subtract (d,e):
    global f        #global means it will be the same value inside the function as well as outside the function
    f = d - e
    return f
subtract(1,2)
print(f)