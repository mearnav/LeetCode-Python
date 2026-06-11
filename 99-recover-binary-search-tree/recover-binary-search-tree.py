# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first_wrong  = None
        second_wrong = None
        prev_node    = [None]

        def in_order_check(node):
            if node is None:                          
                return

            in_order_check(node.left)

            if prev_node[0] and prev_node[0].val > node.val:
                nonlocal first_wrong, second_wrong    

                if first_wrong is None:
                    first_wrong = prev_node[0]
                second_wrong = node

            prev_node[0] = node

            in_order_check(node.right)                

        in_order_check(root)                          

        if first_wrong and second_wrong:
            first_wrong.val, second_wrong.val = second_wrong.val, first_wrong.val