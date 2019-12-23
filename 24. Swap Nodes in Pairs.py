# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#     def __repr__(self):
#         return "ListNode ({})".format(self.val.__repr__())


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        # init
        rs, rs_tail, rs_tail.next = head.next, head, head.next.next
        rs.next = rs_tail
        # loop
        while rs_tail.next and rs_tail.next.next:
            rs_tail.next, rs_tail.next.next, rs_tail.next.next.next = rs_tail.next.next, rs_tail.next, rs_tail.next.next.next
            rs_tail = rs_tail.next.next
        return rs
