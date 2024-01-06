from collections import deque
from typing import List, Tuple, Dict, Optional, Callable

grid_2d = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

grid_2d_4_x_5 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
]

def can_go(grid: List[List], coords: Tuple, cols: int, visited: Dict, values: List) -> Optional[Callable]:
    rows = len(grid)
    not_visited = coords not in visited
    valid_row_idx = coords[0] >= 0 and coords[0] < rows
    valid_col_idx = coords[1] >= 0 and coords[1] < cols
    if not_visited and valid_col_idx and valid_row_idx:
        return lambda: dfs(grid, row=coords[0], col=coords[1], cols=cols, visited=visited, values=values)

# Time: O(n), Space: O(n)
def dfs(grid: List[List], row=0, col=0, cols=None, visited=None, values=None) -> List:
    if visited is None:
        visited = {}
        values = []
        cols = len(grid[0])

    values.append(grid[row][col])
    visited[(row, col)] = True

    # up
    up_coords = (row - 1, col)
    callback = can_go(grid, up_coords, cols, visited, values)
    if callback:
        return callback()

    # right
    right_coords = (row, col + 1)
    callback = can_go(grid, right_coords, cols, visited, values)
    if callback:
        return callback()

    # down
    down_coords = (row + 1, col)
    callback = can_go(grid, down_coords, cols, visited, values)
    if callback:
        return callback()

    # left
    left_coords = (row, col - 1)
    callback = can_go(grid, left_coords, cols, visited, values)
    if callback:
        return callback()

    return values


def has_unvisited_neighbor(coords: Tuple, visited: Dict, grid: List[List[int]]) -> bool:
    cols = len(grid[0])
    rows = len(grid)
    not_visited = coords not in visited
    valid_row_idx = coords[0] >= 0 and coords[0] < rows
    valid_col_idx = coords[1] >= 0 and coords[1] < cols
    if not_visited and valid_row_idx and valid_col_idx:
        return True
    return False

# Time: O(n), Space: O(n)
def bfs(grid: List[List[int]], row=0, col=0):
    values = []
    visited = {}
    queue = deque([(row, col)])
    while queue:
        row, col = queue.popleft()
        values.append(grid[row][col])
        visited[(row, col)] = True

        up_coords = (row - 1, col)
        up_node = has_unvisited_neighbor(up_coords, visited, grid)
        if up_node:
            queue.append(up_coords)
            visited[up_coords] = True

        right_coords = (row, col + 1)
        right_node = has_unvisited_neighbor(right_coords, visited, grid)
        if right_node:
            queue.append(right_coords)
            visited[right_coords] = True

        down_coords = (row + 1, col)
        down_node = has_unvisited_neighbor(down_coords, visited, grid)
        if down_node:
            queue.append(down_coords)
            visited[down_coords] = True

        left_coords = (row, col - 1)
        left_node = has_unvisited_neighbor(left_coords, visited, grid)
        if left_node:
            queue.append(left_coords)
            visited[left_coords] = True

    return values


print(dfs(grid_2d_4_x_5, row=0, col=0))
print(bfs(grid_2d_4_x_5, row=2, col=2))


