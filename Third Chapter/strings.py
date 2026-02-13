# STRINGS

# String is a data type in python.
# String is a sequence of characters enclosed in quotes.
# Strings are immutable



# STRING SLICING

# The index in a sting starts from 0 to (length -1) in Python.
# first index included
# last index not included

c = "caterpillar"
result = c[4]
print(result)

c = "caterpillar"
result = c[5:9]
print(result)

# Word = "amazing"
# Word = [:7] # word [0:7] – 'amazing'
# Word = [0:] # word [0:7] – 'amazing'



# STRING FUNCTIONS

# **Len()**
fruit = "Mango"
print(len(fruit))

# **str.endswith()**
# **str.startswith()**

# Both are CaseSensitive
fruit2 = "banana"
print(fruit2.endswith('na'))


# **str.lower()**
# **str.upper()**
# **str.capitalize()**
# **str.replace()**
# etc...



# ESCAPE SEQUENCE CHARACTERS
# \n --- for newline in the same string
# \t --- for tab space 
# \"wordToBeQuoted\" --- for double quoted string inside string

text = "Lorem Ipsum\n Dolor \"Sit\" Amet"
print(text)
