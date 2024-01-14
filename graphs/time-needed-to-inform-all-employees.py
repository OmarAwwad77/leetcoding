# link: https://leetcode.com/problems/time-needed-to-inform-all-employees/
from typing import List, Dict

def time_to_inform(idx: int, head_idx: int, manager: List[int], inform_time: List[int], cache: Dict[int, int]) -> int:
    if idx in cache: return cache[idx]
    manager_idx = manager[idx]
    val = inform_time[manager_idx] + time_to_inform(manager_idx, head_idx, manager, inform_time, cache)
    cache[idx] = val
    return val

def num_of_minutes(_: int, head_id: int, manager: List[int], inform_time: List[int]) -> int:
    ans = 0
    cache = {head_id: 0}
    for i, t in enumerate(inform_time):
        if not t:
            ans = max(time_to_inform(i, head_id, manager, inform_time, cache), ans)
    return ans
