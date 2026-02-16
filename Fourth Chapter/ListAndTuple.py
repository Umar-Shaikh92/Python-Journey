# LIST
# List, Dictionary, Set  ------ are Mutable Datatypes of python

# List are like array in JS
# List are container to store values of different datatypes

text = ['apple', 23, True, 45.3, None]
print(text[0])
text[0] = "Mango"
print(text)




# LIST METHODS

# append()
friends = ["Abu Bakar", "Umar", "Usman", "Ali"]
friends.append("Ammar")
print(friends)

# sort(): updates the list to [1,2,7,8,15,21]
# reverse(): updates the list to [15,21,2,7,8,1]
# append(8): adds 8 at the end of the list
# insert(3,8): This will add 8 at 3 index
# pop(2): Will delete element at index 2 and return its value.
# remove(21): Will remove 21 from the list. 
# clear(str): Will remove all element from the list. 
# etc....




# TUPLES

# Its Immutable
# Can also take multiple Datatype

# if you want a single element tuple, so make sure to add ',' after that one element
element = (5,)
print(type(element))


elem = ("Bmw", 786, 5.5, True)
print(elem)


# It has only 2 builtin method COUNT & INDEX