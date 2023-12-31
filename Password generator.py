import random
import string

def generate_password():
    password_length = input("Enter the length of the characters: ")
    
    if password_length.isdigit():
        password_length = int(password_length)
        total = string.ascii_letters + string.digits + string.punctuation
        
        password = "".join(random.sample(total, password_length))
        print("Your password is: ")
        print(password)
    else:
        print("Invalid input. Please enter a number.")

generate_password()