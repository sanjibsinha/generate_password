import random
import string

def generate_password(length, use_digits=True, use_special_chars=True):
    characters = string.ascii_letters  # Includes lowercase and uppercase letters

    if use_digits:
        characters += string.digits  # Add digits (0-9)
    
    if use_special_chars:
        characters += string.punctuation  # Add punctuation/special characters

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    # Ask for password length
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 6:
                print("Password length should be at least 6 characters. Try again.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")
    
    # Ask whether to include digits
    use_digits = input("Include digits? (yes/no): ").lower() == "yes"
    
    # Ask whether to include special characters
    use_special_chars = input("Include special characters? (yes/no): ").lower() == "yes"
    
    # Generate the password
    password = generate_password(length, use_digits, use_special_chars)
    
    print(f"Your generated password is: {password}")

if __name__ == "__main__":
    main()