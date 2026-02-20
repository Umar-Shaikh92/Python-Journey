# Write a program to find the greatest of four numbers entered by the user.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if a >= b and a >= c and a >= d:
    print("Greatest number is:", a)

elif b >= a and b >= c and b >= d:
    print("Greatest number is:", b)

elif c >= a and c >= b and c >= d:
    print("Greatest number is:", c)

else:
    print("Greatest number is:", d)

# or

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

print("Greatest number is:", max(a, b, c, d))





# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams.

comment = input("Enter your comment: ")

if ("make a lot of money" in comment.lower() or
    "buy now" in comment.lower() or
    "subscribe this" in comment.lower() or
    "click this" in comment.lower()):
    print("Spam")
else:
    print("Not Spam")





# Write a program to find whether a given username contains less than 10 characters or not.

username = input("Enter a username: ")

if len(username) < 10:
    print("Username contains less than 10 characters")
else:
    print("Username contains 10 or more characters")





# Write a program to calculate the grade of a student from his marks from the
# following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F

marks = int(input("Enter your total marks :"))

if(marks >= 90):
    print("Excellent A+")
elif(marks >= 80):
    print("Grade: A")
elif(marks >= 70):
    print("Grade: B")
elif(marks >= 60):
    print("Grade: C")
elif(marks >= 50):
    print("Grade: D")
else:
    print("Grade: F")