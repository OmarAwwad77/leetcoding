# link: https://leetcode.com/problems/count-complete-tree-nodes/
import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_depth(root: TreeNode, depth=0) -> int:
    if root is None: return depth
    depth += 1
    return get_depth(root.left, depth)

def get_last_lvl_node_by_idx(root: TreeNode, mid, end, start=1) -> Optional[TreeNode]:
    if start == end: return root
    center = math.floor((end + start) / 2)
    if mid <= center:
        return get_last_lvl_node_by_idx(root.left, mid, center, start)
    else:
        return get_last_lvl_node_by_idx(root.right, mid, end, center + 1)

# Time: O(log**2n), Space: O(log n) could be turned to O(1) while loops are used instead of recursion
def count_nodes(root: Optional[TreeNode]) -> int:
    depth = get_depth(root) # log(n)
    if not depth: return depth

    last_lvl_len = pow(2, depth-1)
    upper_nodes_count = last_lvl_len - 1
    last_lvl_count = 1 # we know that at least there could be one element
    left = 1
    right = last_lvl_len

    while left <= right: # log(n/2)
        mid = round((left + right) / 2)
        node = get_last_lvl_node_by_idx(root, mid, last_lvl_len) # log(n)
        if node:
            last_lvl_count = max(last_lvl_count, mid)
            left = mid + 1
        else:
            right = mid - 1
    return upper_nodes_count + last_lvl_count
