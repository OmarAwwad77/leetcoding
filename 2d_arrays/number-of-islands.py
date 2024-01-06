# link: https://leetcode.com/problems/number-of-islands/description/
from collections import deque
from typing import List, Tuple, Dict

Island = Dict[Tuple[int, int], bool]

grid_2d = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
def has_neighbor_land_at(grid: List[List[str]], coords: Tuple[int, int]) -> bool:
    if ((coords[0] >= 0) and (coords[0] < len(grid))) \
            and ((coords[1] >= 0) and (coords[1] < len(grid[0]))) \
            and (grid[coords[0]][coords[1]] == "1"):
        return True
    return False


# DFS solution. Time: O(m*n), Space: O(m*n)
def turn_island_to_water_dfs(grid: List[List[str]], row: int, col: int):
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != '1':
        return
    grid[row][col] = '0'

    turn_island_to_water_dfs(grid, row - 1, col)
    turn_island_to_water_dfs(grid, row, col + 1)
    turn_island_to_water_dfs(grid, row + 1, col)
    turn_island_to_water_dfs(grid, row, col - 1)


# BFS solution. Time: O(m*n), Space: max(m,n)
def turn_island_to_water_bfs(grid: List[List[str]], row: int, col: int):
    queue = deque([(row, col)])
    grid[row][col] = '0'

    while queue:
        row, col = queue.popleft()
        up_coords = (row - 1, col)
        if has_neighbor_land_at(grid, up_coords):
            queue.append(up_coords)
            grid[up_coords[0]][up_coords[1]] = '0'

        right_coords = (row, col + 1)
        if has_neighbor_land_at(grid, right_coords):
            queue.append(right_coords)
            grid[right_coords[0]][right_coords[1]] = '0'

        down_coords = (row + 1, col)
        if has_neighbor_land_at(grid, down_coords):
            queue.append(down_coords)
            grid[down_coords[0]][down_coords[1]] = '0'

        left_coords = (row, col - 1)
        if has_neighbor_land_at(grid, left_coords):
            queue.append(left_coords)
            grid[left_coords[0]][left_coords[1]] = '0'


def num_islands(grid: List[List[str]]) -> int:
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "1":
                turn_island_to_water_bfs(grid, r, c) # or turn_island_to_water_dfs(grid, r, c)
                count += 1
    return count

print(num_islands(grid_2d))


