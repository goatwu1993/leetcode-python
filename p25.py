# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#     def __repr__(self):
#         return "ListNode ({})".format(self.val.__repr__())
from linklist import ListNode, LinkList


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        if k <= 0:
            return None
        if k == 1:
            return head
        tmp = []
        rs = pos = head
        rs_tail = None
        while pos:
            tmp.append(pos)
            pos = pos.next
            if len(tmp) == k:
                tmp.reverse()
                for i in tmp:
                    if rs_tail:
                        rs_tail.next = i
                        rs_tail = rs_tail.next
                    else:
                        rs = rs_tail = i
                rs_tail.next = pos
                tmp = []
        return rs

