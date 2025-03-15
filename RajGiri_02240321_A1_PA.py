import math

def is_prime(number):
    """Checks if a number is prime."""
    if number <= 1:
        return False
    for divisor in range(2, int(math.sqrt(number)) + 1):
        if number % divisor == 0:
            return False
    return True

def calculate_prime_sum():
    """Calculates the sum of prime numbers in a given range."""
    start = int(input("Enter starting number: "))
    end = int(input("Enter ending number: "))
    prime_numbers = [num for num in range(start, end + 1) if is_prime(num)]
    print(f"The prime numbers between {start}-{end}: {prime_numbers}")
    print(f"Total sum: {sum(prime_numbers)}")

def convert_length():
    """Converts length between meters and feet."""
    length = float(input("Enter length value: "))
    unit = input("Convert to (M)eters or (F)eet: ").upper()
    conversion_factors = {'M': 3.28084, 'F': 0.3048}
    if unit in conversion_factors:
        converted = round(length / conversion_factors[unit], 2)
        target_unit = "meters" if unit == 'M' else "feet"
        print(f"Converted length: {converted} {target_unit}")
    else:
        print("Invalid input! Enter 'M' or 'F'.")

def count_consonants():
    """Counts consonants in a given string."""
    text = input("Enter text: ").lower()
    vowels = "aeiou"
    consonant_count = sum(1 for char in text if char.isalpha() and char not in vowels)
    print(f"Number of consonants: {consonant_count}")

def find_min_max():
    """Finds the minimum and maximum number from a list of user-input numbers."""
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print(f"Minimum: {min(numbers)}, Maximum: {max(numbers)}")

def check_palindrome():
    """Checks if a given text is a palindrome."""
    text = input("Enter text: ").lower().replace(" ", "")
    print("Palindrome" if text == text[::-1] else "Not a palindrome")

def word_counter():
    """Counts occurrences of specific words in a text file."""
    words_to_count = ["the", "was", "and"]
    filename = input("Enter the filename: ")
    try:
        with open(filename, 'r') as file:
            text = file.read().lower()
            word_counts = {word: text.split().count(word) for word in words_to_count}
            print("Word Counts:", word_counts)
    except FileNotFoundError:
        print("File not found! Please provide a valid filename.")

def show_menu():
    """Displays a menu and lets the user select a function."""
    menu_options = {
        '1': ("Prime Number Sum", calculate_prime_sum),
        '2': ("Length Converter", convert_length),
        '3': ("Consonant Counter", count_consonants),
        '4': ("Min/Max Finder", find_min_max),
        '5': ("Palindrome Checker", check_palindrome),
        '6': ("Word Counter", word_counter)
    }

    while True:
        print("\nMENU")
        for key, (label, _) in menu_options.items():
            print(f"{key}. {label}")
        print("0. Exit")

        choice = input("\nEnter option: ")
        if choice == '0':
            print("Thanks for using the program!")
            break
        elif choice in menu_options:
            menu_options[choice][1]()  # Calls the selected function
        else:
            print("Invalid option! Please choose 0-6.")

if __name__ == "__main__":
    print("Mathematical and String Processing Functions")
    show_menu()
