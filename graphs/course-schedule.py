# link: https://leetcode.com/problems/course-schedule/description/
from collections import deque, defaultdict
from typing import List


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    adj_list = defaultdict(list)
    visited = {}
    for c, p in prerequisites:
        adj_list[c].append(p)

    while len(visited) != len(adj_list):
        before_len = len(visited)
        for course, preq_list in adj_list.items():
            if course not in visited and all((p not in adj_list or p in visited) for p in preq_list):
                visited[course] = True
        after_len = len(visited)
        if before_len == after_len:
            return False
    return True

# ***********************************************************
def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    graph = [[] for _ in range(num_courses)] # from the question constraints
    for c, p in prerequisites:
        graph[p].append(c)

    for node, connections in enumerate(graph):
        visited = {con: True for con in connections}
        queue = list(connections)
        while queue:
            curr = queue.pop(0)
            for curr_conn in graph[curr]:
                if curr_conn == node:
                    return False
                if curr_conn not in visited:
                    visited[curr_conn] = True
                    queue.append(curr_conn)
    return True




print(can_finish(num_courses=3, prerequisites=[[1,1]]))


