import random
import string

def generate_password(length, complexity):
    # Define character sets based on complexity
    if complexity == 1:
        char_set = string.ascii_lowercase  # Only lowercase letters
    elif complexity == 2:
        char_set = string.ascii_letters  # Lowercase and uppercase letters
    elif complexity == 3:
        char_set = string.ascii_letters + string.digits  # Letters and digits
    else:
        char_set = string.ascii_letters + string.digits + string.punctuation  # Letters, digits, and special characters

    # Generate a random password
    password = ''.join(random.choice(char_set) for _ in range(length))
    return password

def password_generator():
    print("Password Generator")
    
    # Take user input for password length
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length < 1:
                print("Length should be greater than 0. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    # Take user input for password complexity
    print("Select password complexity:")
    print("1. Lowercase Letters")
    print("2. Lowercase and Uppercase Letters")
    print("3. Letters and Digits")
    print("4. Letters, Digits, and Special Characters")
    
    while True:
        try:
            complexity = int(input("Enter your choice (1-4): "))
            if complexity in [1, 2, 3, 4]:
                break
            else:
                print("Invalid choice! Please select a valid complexity (1-4).")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    # Generate and display the password
    password = generate_password(length, complexity)
    print(f"Generated Password: {password}")

# Run the password generator
password_generator()
