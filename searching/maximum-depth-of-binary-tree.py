# link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time: O(n), Space: O(n)
def max_depth(root: Optional[TreeNode]) -> int:
    if not root: return 0
    return max(max_depth(root.left), max_depth(root.right)) + 1