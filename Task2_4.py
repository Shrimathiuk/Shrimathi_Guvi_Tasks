# 4. Write a function that takes a string and returns unique characters in it.

data = input("Enter the string:")
unique_list=[]

def unique():
    for char in data:
        if char not in unique_list:
            unique_list.append(char)


unique()
print("The string is:","".join(unique_list))