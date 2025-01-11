# 9. Write a function that takes a string and returns total number of words in it.
def num_of_words(input):
    x = input.split()
    return len(x)


input = input("Enter the first string: ")

total_words =num_of_words(input)
print("The total number of words :",(total_words))