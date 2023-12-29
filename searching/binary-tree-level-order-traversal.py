# link: https://leetcode.com/problems/binary-tree-level-order-traversal/description/
from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time: O(n), Space: O(n)
def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    result = []
    if not root:return result

    queue = deque()
    queue.append([root])
    while queue:
        curr_level_vals = []
        next_level_nodes = []
        for node in queue.popleft():
            curr_level_vals.append(node.val)
            left = node.left
            right = node.right
            if left is not None:
                next_level_nodes.append(left)
            if right is not None:
                next_level_nodes.append(right)
        if next_level_nodes:
            queue.append(next_level_nodes)
        result.append(curr_level_vals)
    return result


node9 = TreeNode(val=9, left=None, right=None)
node15 = TreeNode(val=15, left=None, right=None)
node7 = TreeNode(val=7, left=None, right=None)
node20 = TreeNode(val=20, left=node15, right=node7)
node3 = TreeNode(val=3, left=node9, right=node20)
print(level_order(node3))
