# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        
        def find(node, remaining, current_path):
            if node is None:
                return

            current_path.append(node.val)
            remaining -= node.val

            if node.left is None and node.right is None and remaining == 0:
                result.append(list(current_path))
            else:
                find(node.left, remaining, current_path)
                find(node.right, remaining, current_path)

            current_path.pop()

        find(root, targetSum, [])
        return result