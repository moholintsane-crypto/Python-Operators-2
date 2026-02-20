# Program to check if a character is an alphabet
char = input("Enter a character: ")

# Using isalpha() to check if it's a letter
if char.isalpha() and len(char) == 1:
    print(f"'{char}' is an alphabet.")
else:
    print(f"'{char}' is not an alphabet.")

# Script to check if a string contains only alphabets
user_input = input("Enter a string: ")

# The .isalpha() method checks for letters A-Z, a-z [7]
if user_input.isalpha():
    print(f"'{user_input}' contains only alphabetic characters.")
else:
    print(f"'{user_input}' contains non-alphabetic characters.")    