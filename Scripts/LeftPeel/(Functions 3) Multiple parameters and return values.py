
print(pow(10, 2))

print(divmod(50, 6))
# Ruturns 2 values in tuples
# 100
# (8, 2)

print('--------------------------')

def sum_up(val1, val2):
    return val1 + val2

print(sum_up(10, 5))
#15

print('--------------------------')

# def sum_up(val1, val2):    
#     return val1 + val2

# print(sum_up(10, 5, 15))
# line 22, 
# in <module>
#     print(sum_up(10, 5, 15))
# TypeError: sum_up() takes 2 positional arguments but 3 were given

print('--------------------------')

def sum_up(val1, val2, val3):   # val3 makes the function fun but it still only returns val1 and val2
    return val1 + val2

print(sum_up(10, 5, 15))
# 15

print('--------------------------')

def sum_up(val1, val2, val3):   
    return val1 + val2 + val3   # now all 3 values/arguments will be added together

print(sum_up(10, 5, 15))
# 30

print('--------------------------')
# Now remember strings are immutable so we need to make a new list to collect to data we want
def remove_mod(string, mod_val):
    new_string = ''
    for index in range(0, len(string)):
        if index % mod_val !=0:
            new_string = new_string + string[index]
    return new_string

a = remove_mod("This is my super awesome string!", 3)
print(a)
# hi i m spe aesmestin!         it has removed every third letter

print('--------------------------')

def hilo(List_of_nums):
    high = float('-inf')    # minus infinity = inf
    low = float("inf")      # infinity = inf
    for index in range(0, len(List_of_nums)):
        if List_of_nums[index] > high:
            high = List_of_nums[index]
        if List_of_nums[index] < low:
            low = List_of_nums[index]
    return high, low

high, low = hilo([5, 3, 1, 2, 3, 5, 10, 15, 20, 25, 0, -16, 10000])
print(high, low)
# 25 0