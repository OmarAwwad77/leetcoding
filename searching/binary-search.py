from typing import List

# Time: O(log n), Space: O(n)
def binary_search(nums: List, target) -> int:
    if not nums: return -1
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = round((left + right) / 2)
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


print(binary_search([0,2,4,6,8,10], target=15))