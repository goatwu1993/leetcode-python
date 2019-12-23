class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return "ListNode ({})".format(self.val.__repr__())

    def create(self, arr):
        rs = pos = None
        for i in arr:
            if not pos:
                pos = ListNode(i)
                rs = pos
            else:
                pos.next = ListNode(i)
                pos = pos.next
        return rs