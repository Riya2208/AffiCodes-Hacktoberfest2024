import random
import string

def generate_password(length):
    if length < 6:
        print("Password length should be at least 6 characters.")
        return None

    # Define possible characters for the password
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Ensure the password contains at least one of each character type
    all_chars = lower + upper + digits + special

    # Select one random character from each category
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    # Fill the rest of the password length with random characters from all categories
    password += random.choices(all_chars, k=length - 4)

    # Shuffle the resulting password list to avoid a predictable pattern
    random.shuffle(password)

    # Convert list to string and return
    return ''.join(password)

# Driver code to test the function
if __name__ == "__main__":
    try:
        length = int(input("Enter the desired password length: "))
        password = generate_password(length)
        if password:
            print("Generated Password: ", password)
    except ValueError:
        print("Please enter a valid number for the password length.")
