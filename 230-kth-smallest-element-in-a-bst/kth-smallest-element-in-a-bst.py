# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrder(self, root):
        elements = []
        if root is None:
            return elements

        if root.left:
            elements += self.inOrder(root.left)

        elements.append(root.val)
            
        if root.right:
            elements += self.inOrder(root.right)
        return elements

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sorted_list = self.inOrder(root)
        return sorted_list[k - 1]