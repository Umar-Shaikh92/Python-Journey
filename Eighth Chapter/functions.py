# A function is a block of code that:
# --Does a specific task
# --Can be reused many times
# --Makes code cleaner and organized


def greet():  # Function Definition
    print("Hello Dear")
    
greet()    # Function Call


# There are two types of functions in python:
# • Built in functions (Already present in python)
# • User defined functions (Defined by the user)
# Examples of built in functions includes len(), print(), range() etc.
# The greet() function we defined is an example of user defined function



# FUNCTIONS WITH PARAMETER
def greet(name):
    print("Hello", name)

greet("Ahmed")



def greetUser(name, ending):
    print("Hello", name, ending)
    print(f"Hello, {name} {ending}")

greetUser("Ahmed", "Thankyou")




# DEFAULT PARAMETER
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Ali")



def func():
    for i in range(3):
        print(i)
        
func()




# RETURN is used to:

# 👉 Send a value back from a function
# 👉 End the function immediately

def test():
    print("Hello")
    return
    print("World")

test()

# Hello  #Output
# print("World") #never runs.

# Because once return is reached → function ends.




def hello():
    print("Hi")

print(hello())   # When a function has no return, Python automatically returns NONE:

# If you don’t want None, just do:
# hello()
# Instead of:
# print(hello())




# RECURSION

# Recursion is a function which calls itself.
# It is used to directly use a mathematical formula as function.

# Every recursive function MUST have:
# --Base Case → When to stop
# --Recursive Case → When to call itself again
# Without base case → infinite loop.



def countdown(n):
    if n == 0:      # Base case, (if no base case the functions become infinite)
        return
    print(n)
    countdown(n - 1)   # Recursive call

countdown(5)


# Down
# Then
# Up
def test(n):
    if n == 0:
        return
    print(n)
    test(n - 1)
    print(n)

test(3)