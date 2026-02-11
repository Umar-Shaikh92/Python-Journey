# BEGIN
print("Hello World")


# MODULE
import pyjokes
jokes = pyjokes.get_joke()
print(jokes)


# PRACTICE SET

# TRIPLE QUOTED STRING
print('''Lorem
      Ipsum
      Dolor
      Amet''')

# EXTERNAL MODULE FOR TEXT TO SPEECH
import pyttsx3
engine = pyttsx3.init()
engine.say("How are you buddy?")
engine.runAndWait()


#  PRINT THE CONTENTS OF THE DIRECTORY USING THE OS MODULE

# Loads Python’s os module
# This module lets Python interact with the operating system(files, folders, paths, etc.)
import os

path = input("Enter the directory path: ")

try:
    contents = os.listdir(path)

    print(f"Contents of '{path}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print("The specified directory does not exist.")
except PermissionError:
    print("You don't have permission to access this directory.")



