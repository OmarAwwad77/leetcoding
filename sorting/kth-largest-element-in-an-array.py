# link: https://leetcode.com/problems/kth-largest-element-in-an-array/description/
from typing import List


# quick-sort solution
class Solution:
    def quick_sort(self, nums: List[int], i=0, p=None):
        initial_i = i
        if p is None:
            p = len(nums) - 1
        if p < i:
            return

        for j in range(i, p):
            if nums[j] <= nums[p]:
                if not i == j:
                    num_i = nums[i]
                    nums[i] = nums[j]
                    nums[j] = num_i
                i += 1

        num_i = nums[i]
        nums[i] = nums[p]
        nums[p] = num_i
        self.quick_sort(nums, i=initial_i, p=i - 1)  # left
        self.quick_sort(nums, i=i + 1, p=p)  # right


    def findKthLargest(self, nums: List[int], k) -> int:
        idx_to_find = len(nums) - k
        self.quick_sort(nums)
        return nums[idx_to_find]


# Hoare's quick-select algorithm
def find_kth_largest(nums: List[int], k: int, i=0, p=None) -> int:
    nums_len = len(nums)
    idx_to_find = nums_len - k
    initial_i = i
    if p is None:
        p = nums_len - 1
    if p < i:
        return

    for j in range(i, p):
        if nums[j] <= nums[p]:
            if not i == j:
                num_i = nums[i]
                nums[i] = nums[j]
                nums[j] = num_i
            i += 1

    num_i = nums[i]
    nums[i] = nums[p]
    nums[p] = num_i

    if idx_to_find == i:
        return nums[i]
    elif idx_to_find < i:
        return find_kth_largest(nums, k, i=initial_i, p=i - 1) # left
    else:
        return find_kth_largest(nums, k, i=i + 1, p=p) # right