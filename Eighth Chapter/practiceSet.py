# Write a program using functions to find greatest of three numbers.

def greatest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
        
print(greatest(1, 2, 3))





# Write a python program using function to convert Celsius to Fahrenheit.

def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Enter temperature in F: "))
c = f_to_c(f)
print(f"{round(c, 2)} ° C")





# How do you prevent a python print() function to print a new line at the end.

print("Hello ", end="")
print("World")





# Write a python function to print first n lines of the following pattern:
# ***
# ** - for n = 3
# *

def pattern(n):
    if (n==0):
        return
    print("*" * n)
    pattern(n-1)
    
pattern(4)





# Write a python function which converts inches to cms.

def inch_to_cms(n):
    return n*2.54

print(f"{inch_to_cms(5)} cm")





# Write a python function to print multiplication table of a given number.

def table(n):
    for i in range(1, 11):
        print(f"{n} X {i} = {n * i}")

table_number = int(input("Enter a number: "))
table(table_number)





# def countdown(n):
#     if n==0:
#         return
#     print(n)
#     countdown(n-1)
    
# countdown(3)