# 7. Write a function that takes string and returns most frequently used character in it.
data = input("Enter the string:")
list1 = []
frequent_list = []

def frequent_character():

    for char in data:
        if char in list1:
            frequent_list.append(char)
        else:
            list1.append(char)

frequent_character()
print("Frequently used character is :",(frequent_list))