# 5. Write a function that takes a string and returns True if Palindrome and False otherwise.
def is_palindrome(input_string):
    reversed_string = input_string[::-1]
    return input_string == reversed_string

data = input("Enter the string: ")

if is_palindrome(data):
    print("True")
else:
    print("False")
