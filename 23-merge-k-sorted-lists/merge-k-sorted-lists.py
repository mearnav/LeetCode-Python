# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        values = []

        for node in lists:
            while node:
                values.append(node.val)
                node = node.next

        values.sort()

        dummy = ListNode(0)
        cur = dummy
        for val in values:
            cur.next = ListNode(val)
            cur = cur.next

        return dummy.next