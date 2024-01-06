# link: https://www.lintcode.com/problem/663/
from typing import List, Tuple

rooms_2d_1 = [
    [2147483647,-1,0,2147483647],
    [2147483647,2147483647,2147483647,-1],
    [2147483647,-1,2147483647,-1],
    [0,-1,2147483647,2147483647]
]

rooms_2d_2 = [[0,-1],[2147483647,2147483647]]

def set_distances_dfs(rooms: List[List[int]], r: int, c: int, steps=0):
    if r < 0 or r >= len(rooms) or c < 0 or c >= len(rooms[0]) or (rooms[r][c] <= steps and steps):
        return
    rooms[r][c] = steps
    steps += 1

    set_distances_dfs(rooms, r - 1, c, steps) # up
    set_distances_dfs(rooms, r, c + 1, steps) # right
    set_distances_dfs(rooms, r + 1, c, steps) # down
    set_distances_dfs(rooms, r, c - 1, steps) # left

# Time: O(n), Space: O(n)
def walls_and_gates(rooms: List[List[int]]):
    for r in range(len(rooms)):
        for c in range(len(rooms[0])):
            if rooms[r][c] == 0:
                set_distances_dfs(rooms, r, c,)

walls_and_gates(rooms_2d_1)
walls_and_gates(rooms_2d_2)
print(rooms_2d_1 == [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]])
print(rooms_2d_2 == [[0,-1],[1,2]])