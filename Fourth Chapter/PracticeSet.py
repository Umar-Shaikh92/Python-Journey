# Write a program to store 5 fruits in a list entered by the user.

cars = []
cars.extend(["Bmw", "BYD", "Porsche", "Ford", "Lamborghini"])
print(cars)




# Write a program to accept marks of 5 students and display them in a sorted manner

marks = []
m1 = int(input("Enter Marks here!"))
m2 = int(input("Enter Marks here!"))
m3 = int(input("Enter Marks here!"))
m4 = int(input("Enter Marks here!"))
m5 = int(input("Enter Marks here!"))
marks.extend([m1, m2, m3, m4, m5])
marks.sort()
print(marks)




# Write a program to sum a list with 4 numbers.

l = [2, 4, 6, 8]
print(sum(l))




# Write a program to count the number of zeros in the following tuple:

a = (7, 0, 8, 0, 0, 9)
print(a.count(0))
