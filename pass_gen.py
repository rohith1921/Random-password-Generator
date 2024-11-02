import random
import string

# Function to generate a random password based on user criteria
def generate_password(length, include_uppercase, include_numbers, include_symbols):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if include_uppercase else ''
    numbers = string.digits if include_numbers else ''
    symbols = string.punctuation if include_symbols else ''

    # Combine all chosen character sets
    all_characters = lower + upper + numbers + symbols

    if not all_characters:
        raise ValueError("No character types selected for password generation.")
    
    # Generate password by randomly selecting from the combined character set
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

# Main function to get user input and generate the password
def main():
    print("Random Password Generator")

    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            raise ValueError("Length should be a positive integer.")

        include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        password = generate_password(length, include_uppercase, include_numbers, include_symbols)
        print(f"Generated Password: {password}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
