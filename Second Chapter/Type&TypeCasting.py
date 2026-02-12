# TYPE
a = "34.3"
print(type(a))

# TYPECASTING
# float(32) => 32.0 # integer to float conversion
# str(31) =>"31" # integer to string conversion
# int("32") => 32 # string to integer conversion

print(float(a))

x = 12
print(float(x))



# INPUT
# It is important to note that the output of input is always a string (even is a number is entered).
# Apko input se hi Integer lena hoga, agr ik dfa input lelia to phr  usko Integer nhi bna skte.
name = input("Whats your name?")
print("Hello", name)

# Not like this;
m = input("Enter First Num: ")
n = input("Enter Second Num: ")
print(int(m + n))

# Like This;
m = int(input("Enter First Num: "))
n = int(input("Enter Second Num: "))
print(m + n)