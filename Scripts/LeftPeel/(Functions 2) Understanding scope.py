# # Functions: len([5, 3, 2]), range(0, 10), pow(5, 3), int("5"), srt(5000)

# # f(x) = 2x
# # 1) Function definition is f(x) = 2x
# # 2) The parameter/value here is x
# # 3) The return value is 2x     (In programming this is optional)

# from sqlite3 import paramstyle

# # Has a parameter and a return value
# def function1(parameter1):
#     return 2 * parameter1

# a = function1(10)   # This puts 10 in as the parameter1 and multiplies it by two.
# print(a)
# # 20

# Has a parameter and no return value
def function2(parameter1):  # May be used to transfer information to a file or server
    print(parameter1)

a = function2(10)
print(a)

# 20    calls function1(10)
# 10    calls function2(10)
# None  returns a none value because there is no value

# Has no parameter and a return value

def function3():    # May be used to pull information from a location

    return 10

a = function3()
print(a)
# 10

# Has no parameter and no return value

def function4():    # May be for printing a menu out
    print("Hi")

function4()
# Hi
