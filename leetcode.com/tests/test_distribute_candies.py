from unittest import TestCase

from distribute_candies import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.distributeCandies([1, 1, 2, 2, 3, 3]), 3)

    def test_1(self):
        self.assertEqual(s.distributeCandies([1, 1, 2, 3]), 2)

    def test_2(self):
        self.assertEqual(s.distributeCandies([1, 1, 1, 1, 2, 2, 2, 3, 3, 3]), 3)
