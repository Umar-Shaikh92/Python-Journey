# Write a program to create a dictionary of Hindi words with values as their English translation. 
# words = {
#     "greet": "salam",
#     "disturb": "pareshan",
#     "work": "kam"
# }

# word = input("Enter a word that meaning you want!")
# print(words[word])





# Write a program to input eight numbers from the user and display all the unique numbers (once).
# numbers = set()

# for i in range(8):
#     num = int(input("Enter a number: "))
#     numbers.add(num)

# print("Unique numbers are:", numbers)





# Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names
friends = {}

name = input("Enter Your Name: ")
language = input("Enter Your Language: ")
friends.update({name: language})

name = input("Enter Your Name: ")
language = input("Enter Your Language: ")
friends.update({name: language})

name = input("Enter Your Name: ")
language = input("Enter Your Language: ")
friends.update({name: language})

name = input("Enter Your Name: ")
language = input("Enter Your Language: ")
friends.update({name: language})

print(friends)









# import tkinter as tk

# root = tk.Tk()

# Widgets are added here

# label = tk.Label(root, text="GeeksForGeeks.org!")
# label.pack()

# root.title("Counting Seconds")
# button = tk.Button(root, text="Stop", width=25, command=root.destroy)
# button.pack()

# root.mainloop()