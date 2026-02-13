# Write a python program to display a user entered name followed by Good Afternoon using input () function.
name = input("Enter Your Name?")
print(f"Good Afternoon {name}")


# Write a program to fill in a letter template given below with name and date.
letter = '''Dear <|Name|>, You are selected! <|Date|>'''
print(letter.replace('<|Name|>', 'Umar').replace('<|Date|>', '12 feb, 2026'))


# Write a program to format the following letter using escape sequence characters.
letter = "Dear Harry,\n \tthis python course is nice.\n Thanks!"
print(letter)
