from unittest import TestCase

from range_addition_ii import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.maxCount(3, 3, [[2, 2], [3, 3]]), 4)

    def test_1(self):
        self.assertEqual(s.maxCount(40000, 40000, []), 40000*40000)

    def test_2(self):
        self.assertEqual(s.maxCount(3, 3, []), 9)

    def test_3(self):
        self.assertEqual(s.maxCount(39999, 39999, [[19999, 19999]]), 399960001)
