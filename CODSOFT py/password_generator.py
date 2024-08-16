import random
import string

def generate_password(min_length, has_number, has_special):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    characters = letters
    if has_number:
        characters += digits
    if has_special:
        characters += special_chars

    pwd = ""
    meets_criteria = False
    pwd_has_number = False
    pwd_has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            pwd_has_number = True
        elif new_char in special_chars:
            pwd_has_special = True

        meets_criteria = True

        if has_number and not pwd_has_number:
            meets_criteria = False
        if has_special and not pwd_has_special:
            meets_criteria = False

    return pwd

# User input
min_length = int(input("Enter the minimum length: "))
has_number = input("Do you want to have numbers (y/n)? ").lower() == 'y'
has_special = input("Do you want to have special characters (y/n)? ").lower() == 'y'

# Generate password
pwd = generate_password(min_length, has_number, has_special)
print("The random generated password is: ",pwd)
