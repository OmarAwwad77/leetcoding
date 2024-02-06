# link: https://leetcode.com/problems/min-cost-climbing-stairs/description/
from typing import List

# recursive **********************************************************
def min_cost_climbing_stairs(cost: List[int], curr=1, before_prev=0, prev=0) -> int:
    if curr == len(cost):
        return min(before_prev, prev)
    if curr == 1:
        prev = cost[curr - 1]
    tmp = prev
    prev = min(cost[curr] + before_prev, cost[curr] + prev)
    before_prev = tmp
    return min_cost_climbing_stairs(cost, curr+1, before_prev, prev)


# iterative **********************************************************
def min_cost_climbing_stairs(cost: List[int]) -> int:
    prev = 0
    before_prev = 0
    for c in cost:
        tmp = prev
        prev = min(c + prev, c + before_prev)
        before_prev = tmp
    return min(prev, before_prev)


# top down solution **************************************************
def min_cost_climbing_stairs(cost: List[int], n=None, cache=None) -> int:
    if n is None:
        cache = {}
        n = len(cost)
        curr_cost = 0
    elif n < 0:
        return 0
    else:
        if n in cache: return cache[n]
        curr_cost = cost[n]
    val = min(min_cost_climbing_stairs(cost, n - 1, cache), min_cost_climbing_stairs(cost, n - 2, cache)) + curr_cost
    cache[n] = val
    return val
