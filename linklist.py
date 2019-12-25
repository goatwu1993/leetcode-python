class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return "ListNode ({}) -> {}".format(self.val.__repr__(), self.next.__repr__())

    def __eq__(self, other):
        return self.val == other.val and self.next == other.next


class LinkList:
    def __init__(self, arr):
        if type(arr) not in [list]:
            raise ValueError('arr should be a iterable object')
        self.root = None
        rs = pos = None
        for i in arr:
            if not pos:
                pos = ListNode(i)
                rs = pos
            else:
                pos.next = ListNode(i)
                pos = pos.next
        self.root = rs
