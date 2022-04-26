# Scope - Where you are able to access a variable


def foo():
    # function scope
    a = 'Hi'
    print(a)    # Doesn't matter that a is not defined at this point because it has not been called.

# File scope - this means it is avaialble to anything after it has been defined
a = 15  # this wont matter because we define a in the function

foo() # Function call
# Hi

print("------------------------------------------------------------------------")

# def foo():
#     print(a)
#     a = 'Hi'
#     print(a)   # This wont work because the function now has its own variable
                 # and cannot print before the defined point in the function

# a = 15 
# foo()

# line 17, in foo
#     print(a)
# UnboundLocalError: local variable 'a' referenced before assignment

# If you create a variable inside and outside the function with the same name then you will have issues

print("------------------------------------------------------------------------")

def foo():
    # function scope
    a = 'Hi'
    print(a)   
# File scope - this means it is avaialble to anything after it has been defined
a = 15

foo()       # once the function is done the file scope takes over so 'a' becomes 15
print(a)
# Hi
# 15

print("------------------------------------------------------------------------")

def foo():
    # function scope
    a = 'Hi'
    print(a)   

def moo():
    print(a)
# File scope - this means it is avaialble to anything after it has been defined
a = 15

foo()       # once the function is done the file scope takes over so 'a' becomes 15
moo()
print(a)
# Hi
# 15
# 15

print("------------------------------------------------------------------------")

def foo():
    # function scope
    a = 'Hi'
    print(a)   

def moo():
    # function scope
    a = 5.6
    print(a)

# File scope - this means it is avaialble to anything after it has been defined
a = 15

foo()       # once the function is done the file scope takes over so 'a' becomes 15
moo()
print(a)
# Hi
# 5.6
# 15