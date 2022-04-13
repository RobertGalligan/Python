def say_something():
    print("Hello world")
def say_name (name):
    print ("Hello " + name)
say_something()
say_name("Jonathan")
say_name("Billy")
doesnt_work()       #this function will not work as it was not defined before it was executed
def doesnt_work():
    print("This doesn't work")