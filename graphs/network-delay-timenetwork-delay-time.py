# link: https://leetcode.com/problems/network-delay-time/description/
from collections import deque, defaultdict
from queue import PriorityQueue
from typing import List, Dict


# bfs ****************************************************************
def network_delay_time_bsf(times: List[List[int]], n: int, k: int) -> int:
    cost = {i: float('INF') if i != k else 0 for i in range(1, n+1)}
    adj_list = defaultdict(list)
    for s, d, c in times:
        adj_list[s].append((d, c))

    queue = deque([k])
    while queue:
        curr = queue.popleft()
        for d, c in adj_list[curr]:
            new_destination_cost = c + cost[curr]
            if new_destination_cost < cost[d]:
                cost[d] = new_destination_cost
                queue.append(d)
    total_cost = max(cost.values())
    return -1 if total_cost == float('INF') else total_cost


# dfs ****************************************************************
def dfs(adj_list: Dict, cost: Dict, node: int):
    curr_cost = cost[node]
    for d, c in adj_list[node]:
        c += curr_cost
        if cost[d] > c:
            cost[d] = c
            dfs(adj_list, cost, d)

def network_delay_time_dfs(times: List[List[int]], n: int, k: int) -> int:
    cost = {i: float('INF') if i != k else 0 for i in range(1, n + 1)}
    adj_list = defaultdict(list)
    for s, d, c in times:
        adj_list[s].append((d, c))

    dfs(adj_list, cost, k)

    total_cost = max(cost.values())
    return -1 if total_cost == float('INF') else total_cost


# Dijkstra's Algorithm ****************************************************************
def network_delay_time(times: List[List[int]], n: int, k: int) -> int:
    cost = {i: float('INF') if i != k else 0 for i in range(1, n + 1)}
    pq = PriorityQueue()
    pq.put((0, k))
    adj_list = defaultdict(list)
    for s, d, c in times:
        adj_list[s].append((d, c))

    while not pq.empty():
        curr_cost, curr_node = pq.get()
        for d, c in adj_list[curr_node]:
            c += curr_cost
            if cost[d] > c:
                cost[d] = c
                pq.put((c, d))
    total_cost = max(cost.values())
    return -1 if total_cost == float('INF') else total_cost


# Bellman-Ford Algorithm ****************************************************************
def network_delay_time(times: List[List[int]], n: int, k: int) -> int:
    cost = [0 if i+1 == k else float('INF') for i in range(n)]
    for _ in range(n-1):
        value_changed = False
        for s, d, c in times:
            if cost[s-1] < float('INF'):
                c += cost[s-1]
                if cost[d-1] > c:
                    cost[d-1] = c
                    value_changed = True
        if not value_changed: break
    total_cost = max(cost)
    return -1 if total_cost == float('INF') else total_cost
