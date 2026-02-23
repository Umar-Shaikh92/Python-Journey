# Python has 2 main loops:
# 1) for loop
# 2) while loop


# FOR LOOP
# Used when we know how many times we want to repeat.
# A for loop is used to iterate through a sequence like list, tuple, or string [iterables]

l = [1, "hello", 8]
for item in l:
 print(item)
 
 
#  Range function in python
# range(start, stop, step_size)

for i in range(0, 5):
    print(i)
    
for i in range(1, 10, 2):
    print(i)
    
# An optional else can be used with a for loop if the code is to be executed when the loops exhausts.
l = [1, 5, 'hola', 9]
for item in l:
    print(item)
else:
    print("Done")
    
    
    
# BREAK 
# stops the loop immediately. It instruct the program to exit the operation now

for i in range(10):
    if i == 5:
        break
    print(i)
    
    
    
# CONTINUE
# It is used to stop the current iteration of the loop and continue with the next one. It instructs the Program to “skip this iteration”.

for i in range(10):
    if i == 5:
        continue
    print(i)




# WHILE LOOP
# Used when we repeat until a condition become false

i = 1
while i <= 5:
    print(i)
    i += 1




# QUICK QUIZE
l = ['Apple', 5, True, 'Ijaz']
i = 0
while (i<len(l)):
    print(l[i])
    i+=1