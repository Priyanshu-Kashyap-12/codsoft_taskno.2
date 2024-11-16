# Password Generator

# Introduction:
# This program generates a strong, random password based on user input for the number of letters, digits, and symbols.
# It uses Python's `random` and `string` modules for secure and randomized password generation.

# Required libraries
import random
import string

start = 1
while start > 0:

    # Password Components:
    # Explain that the program uses letters, digits, and symbols to create a customizable password.
    letters = string.ascii_letters  # Includes both uppercase and lowercase letters.
    digits = string.digits          # Includes digits from 0-9.
    symbols = string.punctuation    # Includes special characters like @, #, $, etc.

    # Input for each component:
    print("Give required input for generating a password")
    pass_letters = int(input("Enter number of letters: "))
    pass_digits = int(input("Enter number of digits: "))
    pass_symbols = int(input("Enter number of symbols: "))

    # Password Generation:
    # Highlight how the program generates random characters for each component and combines them.
    letters_pass = [random.choice(letters) for _ in range(pass_letters)]  # Randomly select letters.
    digits_pass = [random.choice(digits) for _ in range(pass_digits)]    # Randomly select digits.
    symbols_pass = [random.choice(symbols) for _ in range(pass_symbols)] # Randomly select symbols.

    # Combine all components and shuffle for randomness:
    password = letters_pass + digits_pass + symbols_pass
    random.shuffle(password)  # Shuffle to avoid predictable patterns.
    password = ''.join(password)  # Join the list into a single string.

    # Display Password:
    print(f"Your Generated Password: {password}")  # Show the generated password to the user.

    # Conclusion:
    # Demonstrate how the program allows users to generate multiple passwords or exit by entering 'n'.
    choice = input("For stopping here, enter 'n'. To generate another password, enter any other key: ")
    if choice == "n":
        break
    start += 1

# End of the program
# Conclusion in the video: This program is a simple yet effective tool for creating secure passwords.
