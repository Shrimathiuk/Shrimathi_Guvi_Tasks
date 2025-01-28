# Task 3_9: Find triplet with a given sum
print("\n\nFind triplet with a given sum\n")
def find_triplet(nums, target):
    nums.sort()
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == target:
                return (nums[i], nums[left], nums[right])
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    return None

nums = [10, 20, 30, 9]
target = 59
print("Triplet:", find_triplet(nums, target))
