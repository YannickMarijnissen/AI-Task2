import itertools

# Function to solve a cryptarithmetic puzzle
def solve_cryptarithmetic(word1, word2, result):
    # Create a set of unique characters in all words
    unique_chars = set(word1 + word2 + result)
    
    # Check if there are more than 10 unique characters (0-9 digits)
    if len(unique_chars) > 10:
        print("Invalid input: More than 10 unique characters")
        return

    # Convert unique characters to a list and create a range of digits (0-9)
    chars = list(unique_chars)
    digits = range(10)
    
    # Iterate through all permutations of digits for unique characters
    for perm in itertools.permutations(digits, len(unique_chars)):
        char_to_digit = {char: digit for char, digit in zip(chars, perm)}
        
        # Check if leading zeros are assigned to the words
        if char_to_digit[word1[0]] == 0 or char_to_digit[word2[0]] == 0 or char_to_digit[result[0]] == 0:
            continue

        # Convert words to numbers using the character-to-digit mapping
        num1 = int(''.join(str(char_to_digit[char]) for char in word1))
        num2 = int(''.join(str(char_to_digit[char]) for char in word2))
        res = int(''.join(str(char_to_digit[char]) for char in result))

        # Check if the addition of num1 and num2 equals res
        if num1 + num2 == res:
            num_mapping = {char: char_to_digit[char] for char in chars}
            # Print the solution with numbers and the number correspondence
            print(f"Solution found: {word1} + {word2} = {result} ({num1} + {num2} = {res})")
            print("Number Correspondence:")
            for char, digit in num_mapping.items():
                print(f"{char} = {digit}")
            return

    # If no solution is found, print a message
    print("No solution found")

if __name__ == "__main__":
    # Get user input for the cryptarithmetic puzzle
    puzzle = input("Enter the cryptarithmetic puzzle (e.g., 'TO + GO = OUT'): ")
    parts = puzzle.split()
    
    # Check if the input format is valid
    if len(parts) != 5 or parts[1] != '+' or parts[3] != '=':
        print("Invalid input format. Please use the format 'WORD1 + WORD2 = RESULT'.")
    else:
        word1, word2, result = parts[0], parts[2], parts[4]
        # Call the solve_cryptarithmetic function to solve the puzzle
        solve_cryptarithmetic(word1, word2, result)

