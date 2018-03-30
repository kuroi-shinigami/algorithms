from unittest import TestCase

from non_decreasing_array import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.checkPossibility([4, 2, 3]), True)

    def test_1(self):
        self.assertEqual(s.checkPossibility([4, 2, 1]), False)

    def test_2(self):
        self.assertEqual(s.checkPossibility([3, 4, 2, 3]), False)

    def test_3(self):
        self.assertEqual(s.checkPossibility([1]), True)

    def test_4(self):
        self.assertEqual(s.checkPossibility([-1, 4, 2, 3]), True)

    def test_5(self):
        self.assertEqual(s.checkPossibility([1, 2, 5, 4, 3]), False)
