# https://leetcode.com/problems/two-sum/
from typing import List, Dict


# brute-force Time: O(n*2), Space: O(1)
def two_sum(nums: List[int], target: int):
    for i, n in enumerate(nums):
        for i2 in range(i+1, len(nums)):
            n2: int = nums[i2]
            if n + n2 == target: return i, i2

# optimal Time: O(n), Space: O(n)
def two_sum(nums: List[int], target: int):
    second_pairs: Dict[int, int] = {}
    for i, n in enumerate(nums):
        if n in second_pairs:
            return second_pairs[n], i
        second_pairs[target - n] = i


print(two_sum([3,3], 6))

