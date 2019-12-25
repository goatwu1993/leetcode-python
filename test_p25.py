import unittest
from p25 import Solution
from linklist import LinkList, ListNode


class SolutionTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(
            LinkList([3, 2, 1, 6, 5, 4, 7]).root,
            Solution().reverseKGroup(LinkList([1, 2, 3, 4, 5, 6, 7]).root, 3)
        )
        self.assertEqual(
            LinkList([1, 2, 3, 4, 5, 6, 7]).root,
            Solution().reverseKGroup(LinkList([1, 2, 3, 4, 5, 6, 7]).root, 1)
        )
        self.assertEqual(
            LinkList([1, 2, 3, 4, 5, 6, 7]).root,
            Solution().reverseKGroup(LinkList([1, 2, 3, 4, 5, 6, 7]).root, 11)
        )

    def test2(self):
        self.assertEqual(
            LinkList([]).root,
            Solution().reverseKGroup(LinkList([]).root, 3)
        )
