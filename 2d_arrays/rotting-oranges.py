# link: https://leetcode.com/problems/rotting-oranges/
from collections import deque
from typing import List, Tuple


# Time: O(n), Space: O(n)
def orange_rotting(grid: List[List[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    minutes = 0
    fresh_count = 0
    queue = deque()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                fresh_count += 1
            elif grid[r][c] == 2:
                queue.append((r, c))
    if not fresh_count: return 0

    while queue:
        queue_len = len(queue)
        for i in range(queue_len):
            row, col = queue.popleft()
            up_coords = (row - 1, col)
            if is_fresh_orange(grid, up_coords):
                queue.append(up_coords)
                grid[up_coords[0]][up_coords[1]] = 2
                fresh_count -= 1

            right_coords = (row, col + 1)
            if is_fresh_orange(grid, right_coords):
                queue.append(right_coords)
                grid[right_coords[0]][right_coords[1]] = 2
                fresh_count -= 1

            down_coords = (row + 1, col)
            if is_fresh_orange(grid, down_coords):
                queue.append(down_coords)
                grid[down_coords[0]][down_coords[1]] = 2
                fresh_count -= 1

            left_coords = (row, col - 1)
            if is_fresh_orange(grid, left_coords):
                queue.append(left_coords)
                grid[left_coords[0]][left_coords[1]] = 2
                fresh_count -= 1
        if queue:
            minutes += 1
    return minutes if not fresh_count else -1


def is_fresh_orange(grid: List[List[int]], coords: Tuple[int, int]):
    if (coords[0] >= 0 and coords[0] < len(grid)) \
            and (coords[1] >= 0 and coords[1] < len(grid[0])) \
            and grid[coords[0]][coords[1]] == 1:
        return True
    return False

print(orange_rotting([[2,1,1],[1,1,0],[0,1,1]]))