# Task 3_7: First non-repeating element
print("\n\nFirst non-repeating element\n")


#Finds the first non-repeating element in a given list

def first_non_repeating_element(arr):
    count = {}
    for num in arr:
        count[num] = count.get(num, 0) + 1

    for num in arr:
        if count[num] == 1:
            return num

    return None

# Example:
my_list = [1, 2, 3, 2, 1, 4, 5, 4]
result = first_non_repeating_element(my_list)

if result:
    print("The first non-repeating element is:", result)
else:
    print("All elements repeat.")
