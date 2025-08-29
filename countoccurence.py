# with string functions
# import string
# x="apple"
# for i in x:
#     y=x.count(i)
#     print(str(i)+" has occurred" + str(y) +" times")

# without count functions   

def count_letters(input_string):
    # Initialize an empty dictionary to store letter counts
    letter_counts = {}

    # Iterate through each character in the input string
    for char in input_string:
        # Check if the character is a letter
        if char.isalpha():
            # Convert the letter to lowercase for case-insensitivity
            char = char.lower()

            # Update the letter count in the dictionary
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1

    # Print the letter counts
    for letter, count in letter_counts.items():
        print(f"{letter}: {count}")

# Example usage
input_string = "Hello, World!"
count_letters(input_string)
