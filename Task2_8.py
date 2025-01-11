# 8. Write a function that takes a string and returns true if it is anagram of another string ,otherwise false.
from collections import Counter
def are_anagrams(str1, str2):
    return Counter(str1) == Counter(str2)

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if are_anagrams(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")