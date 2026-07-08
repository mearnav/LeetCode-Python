# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy

        for _ in range(left-1):
            pre = pre.next
        
        cur = pre.next

        for _ in range(right-left):
            next_node = cur.next
            cur.next = next_node.next
            next_node.next = pre.next
            pre.next = next_node

        return dummy.next