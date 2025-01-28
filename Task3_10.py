# Task 3_10: Check for a sublist with a sum of zero
print("\n\nCheck for a sublist with a sum of zero\n")

def has_zero_sum_sublist(nums):

    seen_sums = set()
    current_sum = 0
    for num in nums:
        current_sum += num
        if current_sum == 0 or current_sum in seen_sums:
            return True  # Found a sublist with sum 0
        seen_sums.add(current_sum)
    return False


# Example
nums = [4, 2, -3, 1, 6]

# Check and print if there is any sublist with sum 0
print("Sublist with sum 0 exists:", has_zero_sum_sublist(nums))