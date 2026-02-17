# DICTIONARY

# Like Object in Javascript
# Dictionary is a collection of keys-value pairs.
# It is unordered.
# It is mutable.
# It is indexed.
# Cannot contain duplicate keys.


a = {
"key": "value",
"language": "python",
"marks": "100",
"list": [1, 2, 3]
}
print(a["key"])
print(a["list"])

print(a)




# DICTIONARY METHODS
print(a.items())   #Returns a list of (key,value)tuples
print(a.keys())    #Returns a list containing dictionary's keys
print(a.values())
print(a.update({"language" : "Javascript"}))
print(a)

print(a.get("marks"))
print(a.pop("key"))   #Remove particular key
print(a)

print(a.copy())     #create shallow copy of dictiosnry




# Litte bit of for looop
for key, value in a.items():
    print(key, value)

