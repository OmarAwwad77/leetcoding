# link: https://leetcode.com/problems/container-with-most-water/
from typing import List


# brute-force Time: O(n*2), Space: O(1)
def max_area(height: List[int]):
    max_area_found = 0
    length = len(height)
    for i, h in enumerate(height):
        for i2 in range(i+1, length):
            h2 = height[i2]
            horizontal = i2 - i
            vertical = min(h, h2)
            max_area_found = max(max_area_found, horizontal * vertical)
    return max_area_found

# optimal Time O(n), Space O(1)
def max_area(height: List[int]):
    max_area_found = 0
    start_idx = 0
    end_idx = len(height) - 1

    while end_idx > start_idx:
        horizontal = end_idx - start_idx
        vertical = min(height[start_idx], height[end_idx])
        max_area_found = max(max_area_found, horizontal * vertical)
        if height[start_idx] > height[end_idx]:
            end_idx -= 1
        else:
            start_idx += 1
    return max_area_found


print(max_area([1,8,6,2,5,4,8,3,7]))
