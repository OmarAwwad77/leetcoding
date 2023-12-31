# link: https://leetcode.com/problems/validate-binary-search-tree/
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(root: Optional[TreeNode], prev_min=float('-inf'), prev_max=float('inf')) -> bool:
    if not root: return True
    if root.val <= prev_min or root.val >= prev_max:
        return False
    if not is_valid_bst(root.left, prev_min, root.val): # left
        return False
    return is_valid_bst(root.right, root.val, prev_max) # right


def is_valid_bst(root: Optional[TreeNode], minmax=[]) -> bool:
    if not root: return True
    left_minmax = []; right_minmax = []
    if not is_valid_bst(root.left, left_minmax) or (left_minmax and max(left_minmax) >= root.val):
        return False
    if not is_valid_bst(root.right, right_minmax) or (right_minmax and min(right_minmax) <= root.val):
        return False
    left_right_minmax = [*left_minmax, root.val, *right_minmax]
    if left_right_minmax: minmax.extend([min(left_right_minmax), max(left_right_minmax)])
    return True


