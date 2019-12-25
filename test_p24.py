import unittest
from p24 import Solution
from linklist import LinkList, ListNode


class SolutionTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            LinkList([2, 1, 4, 3]).root,
            Solution().swapPairs(LinkList([1, 2, 3, 4]).root)
        )
