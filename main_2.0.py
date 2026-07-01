import random  # Imports the random module for choosing characters randomly
import string  # Imports the string module for character sets


def generate_password(length):
    if length < 4:  # Checks whether the password length is too short
        print("Password length should be at least 4 characters.") 
        return None  

    lowercase = string.ascii_lowercase 
    uppercase = string.ascii_uppercase  
    digits = string.digits  
    special = string.punctuation  

    required = [  # Creates a list with at least one character from each required category
        random.choice(lowercase),  
        random.choice(uppercase),  
        random.choice(digits),  
        random.choice(special), 
    ]

    all_characters = lowercase + uppercase + digits + special  # Combines all allowed characters
    remaining = [random.choice(all_characters) for _ in range(length - 4)]  # Fills the rest of the password with random characters
    password_chars = required + remaining  # Combines the required characters with the extra ones
    random.shuffle(password_chars)  # Randomizes the order of characters

    return "".join(password_chars)  # Joins the characters into a single password string


print("\nWelcome to the Password Generator!")  # Prints a welcome message
length = int(input("\nEnter the desired length of the password: "))  # Gets the password length from the user

password = generate_password(length)  # Calls the generator function with the entered length
print("\nGenerated Password:", password)
