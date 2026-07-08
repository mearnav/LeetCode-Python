# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def split_into_two_halves(self, head):
        if head is None or head.next is None:
            return head, None

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        second_half = slow.next
        slow.next = None

        return head, second_half

    def merge_sorted_lists(self, head1, head2):
        dummy = ListNode(0)
        tail = dummy

        while head1 and head2:
            if head1.val <= head2.val:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next

        tail.next = head1 if head1 else head2

        return dummy.next


    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        left_head, right_head = self.split_into_two_halves(head)

        left = self.sortList(left_head)
        right = self.sortList(right_head)

        return self.merge_sorted_lists(left, right)