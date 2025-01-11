def count_vowels_and_words(input_string):
    vowels = 'aeiou'
    input_string = input_string.lower()

    # Initialize a dictionary to count each vowel
    vowel_count = {vowel: 0 for vowel in vowels}

    # Count the total number of vowels
    total_vowels = 0
    for char in input_string:
        if char in vowels:
            vowel_count[char] += 1
            total_vowels += 1

    # Split the string into words and count each word
    words = input_string.split()
    word_count = {word: words.count(word) for word in set(words)}

    return total_vowels, vowel_count, word_count


# Example usage
input_string = "Guvi Geeks Network Private Limited"
total_vowels, vowel_count, word_count = count_vowels_and_words(input_string)

print(f"Total number of vowels: {total_vowels}")
print(f"Count of each vowel: {vowel_count}")
