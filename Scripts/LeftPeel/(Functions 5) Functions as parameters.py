
def sum_up(val1, val2):
    return val1 + val2

def do_something(foo, val1, val2):
    result = foo(val1, val2)    # foo has not been determined yet
                                # which means foo can be any function that takes 2 parameter
    return result   

def product_up(val1, val2):
    return val1 * val2

def double_function(foo, val1, val2):
    result = foo(val1, val2) + foo(val1, val2)
    return result    # foo has not been determined yet


print(sum_up(5, 2))
# 7

print(do_something(sum_up, 5, 2))   # foo becomes sum_up
# 7
# you can use any function that takes to parameters and put it in foos place.
print(do_something(pow, 5, 2))   # foo becomes pow
# 25
print(do_something(divmod, 5, 2)) 
(2, 1)
print(do_something(product_up, 5, 2))  
# 10
print(double_function(product_up, 5, 2)) 
# 20
print(double_function(pow, 5, 2))
# 50
print(double_function(sum_up, 5, 2))  
# 14

def double_function2(foo1, foo2, val1, val2):
    result = foo1(val1, val2) + foo2(val1, val2)
    return result 

print(double_function2(sum_up, product_up, 5, 2))  
# 17
print(double_function2(sum_up, pow, 5, 2))  
# 32