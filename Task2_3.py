# 3. Write a function that takes a string and returns a new string with all the vowels removed.
data = input("Enter the string:")

vowel_list = []
consonants = []

def alphabets():
    vowels = ['a', 'e', 'i', 'o', 'u']

    for char in data:
        if char in vowels:
            vowel_list.append(char)
        else:
            consonants.append(char)



alphabets()
print("String without vowels is :", "".join(consonants))
