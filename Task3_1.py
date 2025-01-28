# Task 3_1: Create separate lists for even and odd numbers
from multiprocessing.reduction import duplicate
print("\nCreate separate lists for even and odd numbers")
nums =[10, 501, 22, 37, 100, 999, 87, 351]

even_number = []
odd_number = []
for enum in nums:
    if enum % 2 == 0:
        even_number.append(enum)
    else:
        odd_number.append(enum)

print("Numbers in the list", nums)
print("Even Number : ",even_number)
print("Odd Number : ",odd_number)