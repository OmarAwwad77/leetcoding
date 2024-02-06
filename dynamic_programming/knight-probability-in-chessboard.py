# link: https://leetcode.com/problems/knight-probability-in-chessboard/description/
from collections import deque

# bottom-up recursive solution
def knight_probability(n: int, k: int, row: int, col: int, cache=None) -> float:
    if row < 0 or row >= n or col < 0 or col >= n:
        return 0
    if k == 0:
        return 1
    if cache is None:
        cache = {}
    if (row, col, k) in cache:
        return cache[(row, col, k)]

    prop = 0
    possible_moves = [(-2, -1), (-2, 1),(-1, 2), (1, 2),(2, -1), (2, 1),(-1, -2), (1, -2)]

    for r, c in possible_moves:
        prop += knight_probability(n, k-1, row+r, col+c, cache) / 8

    cache[(row, col, k)] = prop
    return prop

