# link: https://leetcode.com/problems/binary-tree-right-side-view/
from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS Time: O(n), Space: O(n)
def right_side_view(root: Optional[TreeNode]) -> List[int]:
    result = []
    if not root: return result

    result.append(root.val)
    right_branch = right_side_view(root.right)
    left_branch = right_side_view(root.left)
    right_branch.extend(left_branch[len(right_branch):])
    result.extend(right_branch)

    return result

# DFS (extra parameters)
def right_side_view(root: Optional[TreeNode], curr_lvl=1, max_lvl=0) -> List[int]:
    result = []
    if not root: return result
    if curr_lvl > max_lvl:
        result.append(root.val)
        max_lvl = curr_lvl
    curr_lvl += 1

    right_branch = right_side_view(root.right, curr_lvl, max_lvl)
    left_branch = right_side_view(root.left, curr_lvl, max_lvl + len(right_branch))
    result.extend(right_branch)
    result.extend(left_branch)

    return result

# BFS Time: O(n), Space: O(n)
def right_side_view(root: Optional[TreeNode]) -> List[int]:
    result = []
    if not root: return result

    queue = deque([root])
    while queue:
        curr_level_len = len(queue)
        for i in range(curr_level_len):
            curr_node = queue.popleft()
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
            if i == curr_level_len - 1:
                result.append(curr_node.val)

    return result

