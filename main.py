import string
import random

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 characters.")
        return None
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
        letters = random.choices(characters, k=length)
        password = ''.join(random.choices(letters, k=length))
        return password


print("\nWelcome to the Password Generator!")
length = int(input("\nEnter the desired length of the password: "))

password: str = generate_password(length)
print("\nGenerated Password:", password)
