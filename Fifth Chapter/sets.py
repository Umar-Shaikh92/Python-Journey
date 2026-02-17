# SETS

# Mutable
# Sets are unordered => Element’s order doesn’t matter
# Sets are unindexed => Cannot access elements by index
# There is no way to change items in sets.
# Not contain duplicate values




# How to Create an Empty Set
s = {}        #This creates an empty dictionary, NOT a set.
s = set()     #This is correct.


s = {2, 4, 6, 8, 10, 12}


# SETs METHOD
s.add("hola")  #Add single item
print(s)

s.update([3, 4])   #Add multile items
print(s)

print(len(s))

s.remove(6)   #Removes element (Error if not found).
print(s)

s.discard(10)   #Removes element (No error if not found).
print(s)

s.clear()
print(s)

s.pop()   #It remove random element from set






# UNION INTERSECTION

s1 = {12, 1, 10, 45, 3}
s2 = {2, 5, 27, 12, 72}

print(s1 | s2)
# or
print(s1.union(s2))    #In the case of UNION we have to write all elements of set1 & set2


print(s1 & s2)
# or
print(s1.intersection(s2))    #In the case of INTERSECTION we have to write elements that are similar in set1 & set2





s = {False, 0}
print(s)    #Return False because false = 0 and true = 1