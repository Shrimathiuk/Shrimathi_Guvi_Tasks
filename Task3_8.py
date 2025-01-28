# Task 3_8: Find minimum element in a sorted list
print("\n\nFind minimum element in a sorted list\n")

print("Using min method")
sorted_list = [10, 20, 30, 40, 50]
print("Minimum Element:", min(sorted_list))

print("\nUsing for loop")
min_val = sorted_list[0]  # Initialize with the first element
for num in sorted_list:
    if num < min_val:
        min_val = num
print("Minimum number in the list: ",min_val)