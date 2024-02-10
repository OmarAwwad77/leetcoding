# link: https://leetcode.com/problems/house-robber/description/
from collections import defaultdict
from typing import List


class RecursiveSolution:
    def rob(self, nums: List[int], idx=0, cache=None) -> int:
        if cache is None:
            cache = {}
        if idx in cache:
            return cache[idx]
        if idx >= len(nums):
            return 0

        ans = max(self.rob(nums, idx + 1, cache), self.rob(nums, idx + 2, cache) + nums[idx])
        cache[idx] = ans
        return ans

class IterativeSolution:
    def rob(self, nums: List[int]) -> int:
        cache = defaultdict(int)
        for idx in range(len(nums) - 1, -1, -1):
            cache[idx] = max(cache[idx+1], nums[idx]+ cache[idx+2])
        return cache[0]


