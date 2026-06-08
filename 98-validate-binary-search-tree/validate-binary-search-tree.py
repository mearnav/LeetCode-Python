# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root, min_allowed=float('-inf'), max_allowed=float('inf')):
        if root is None:
            return True

        if root.val <= min_allowed or root.val >= max_allowed:
            return False

        left_ok = self.isValidBST(root.left, min_allowed, root.val)
        right_ok = self.isValidBST(root.right, root.val, max_allowed)

        return left_ok and right_ok
