# https://www.youtube.com/watch?v=-qOVVRIZzao&ab_channel=AbdulBari
from typing import List
def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

def get_partition(nums, left, right):
    pivot_element = nums[right]
    partition_idx = left

    for j in range(left, right):
        if nums[j] <= pivot_element:
            swap(nums, partition_idx, j)
            partition_idx += 1
    swap(nums, partition_idx, right)
    return partition_idx

def quick_sort(nums, left, right):
    if left < right:
        partition_idx = get_partition(nums, left, right)
        quick_sort(nums, left, partition_idx - 1)
        quick_sort(nums, partition_idx + 1, right)


def quick_sort_2(nums: List[int], i=0, p=None):
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
    quick_sort(nums, i=initial_i, p=i-1) # left
    quick_sort(nums, i=i+1, p=p) # right


def quick_sort_3(nums: List[int], i=None, p=None):
    if i is None:
        p = len(nums) - 1
        i = 0
    if p - i < 1:
        return

    initial_i = i
    initial_p = p
    while not p == i:
        p_num = nums[p]
        i_num = nums[i]

        if i_num > p_num:
            if not p - 1 == i:
                before_p_num = nums[p - 1]
                nums[p - 1] = p_num
                nums[p] = nums[i]
                nums[i] = before_p_num
            else:
                nums[i] = p_num
                nums[p] = i_num
            p -= 1
            continue
        i += 1

    quick_sort(nums, i=initial_i, p=max(p-1, initial_i)) # left
    quick_sort(nums, i=min(p+1, initial_p), p=initial_p) # right


