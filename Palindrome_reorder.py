from collections import Counter

s = input()  # Input string
freq = Counter(s)  # Count character frequencies

# Find characters with odd frequencies
odd_chars = [char for char, count in freq.items() if count % 2 != 0]

# More than one odd count => palindrome impossible
if len(odd_chars) > 1:
    print("NO SOLUTION")
else:
    first_half = []  # First half of palindrome
    middle_char = ''  # Middle character (if any)

    # Construct first half and determine middle character
    for char in sorted(freq.keys()):  # Sort for deterministic output
        count = freq[char]
        first_half.append(char * (count // 2))  # Half count for first half

        if count % 2 != 0:  # If odd, character goes in the middle (once)
            middle_char = char

    first_half_str = ''.join(first_half)  # First half as string
    second_half_str = first_half_str[::-1]  # Mirror first half

    # Output the complete palindrome
    print(first_half_str + (middle_char if middle_char else '') + second_half_str)



