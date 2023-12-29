# link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
from typing import List

# optimal. Time: O(log n), Space: O(log n)
def search_range(nums: List[int], target: int, left=0, right=None) -> List[int]:
    if right is None:
        right = len(nums) - 1
    if left > right: return [-1, -1]

    mid = round((left + right) / 2)
    if nums[mid] == target:
        indices = [mid]
        left_side = search_range(nums, target, left=left, right=mid - 1)
        right_side = search_range(nums, target, left=mid + 1, right=right)
        if not left_side == [-1, -1]:
            indices.extend(left_side)
        if not right_side == [-1, -1]:
            indices.extend(right_side)
        return [min(indices), max(indices)]
    elif nums[mid] > target:
        return search_range(nums, target, left=left, right=mid - 1)
    else:
        return search_range(nums, target, left=mid + 1, right=right)

print(search_range([5,7,7,8,8,10], target=8))

