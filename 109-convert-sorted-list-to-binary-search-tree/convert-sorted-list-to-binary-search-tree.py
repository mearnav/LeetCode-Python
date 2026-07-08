# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sorted_array_to_bst(self, arr):
        if not arr:
            return None

        mid = len(arr) // 2
        node = TreeNode(arr[mid])

        node.left = self.sorted_array_to_bst(arr[:mid])
        node.right = self.sorted_array_to_bst(arr[mid+1:])

        return node

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        values = []

        current = head
        while current:
            values.append(current.val)
            current = current.next

        return self.sorted_array_to_bst(values)