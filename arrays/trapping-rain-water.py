# link: https://leetcode.com/problems/trapping-rain-water/
from typing import List

# brute-force Time: O(n*2), Space: O(n)
def trap(height: List[int]):

    area = 0
    for i, w in enumerate(height):
        right_max = max([*height[i + 1:], 0])
        left_max = max([*height[:i] ,0])
        water_above = max(min(right_max, left_max) - w, 0)
        area += water_above
    return area


# optimal Time: O(n), Space: O(n)
def trap(height: List[int]):
    area = 0
    curr_v = 0
    direction = None # 0 left , 1 right
    start_idx = 0
    end_idx = len(height) - 1

    while end_idx > start_idx:
        if direction is not None:
            if direction == 0:
                wall = height[start_idx]
            else:
                wall = height[end_idx]
            area -= min(curr_v, wall)

        v = min(height[start_idx], height[end_idx])
        if v > curr_v:
            h = (end_idx - start_idx) - 1
            area += (v - curr_v) * h
            curr_v = v

        if height[start_idx] > height[end_idx]:
            end_idx -= 1
            direction = 1
        else:
            start_idx += 1
            direction = 0

    return area

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
