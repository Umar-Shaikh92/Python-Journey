# "r"  --- 	Read (file read karne ke liye)
# "w"  ---	Write (nayi file banata hai ya purani overwrite karta hai)
# "a"	 ---    Append (file ke end me add karta hai)
# "r+"  ---  Read + Write

# It create a file and write content
name = input ("Enter your name: ")

with open("name.txt", "a") as file:
    file.write(name + "\n")


# It write all the  file content
# with open("name.txt", "r") as file:
#     data = file.read()
#     print(data)