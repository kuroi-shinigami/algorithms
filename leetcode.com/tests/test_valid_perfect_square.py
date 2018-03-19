from unittest import TestCase

from valid_perfect_square import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.isPerfectSquare(16), True)

    def test_1(self):
        self.assertEqual(s.isPerfectSquare(14), False)

    def test_2(self):
        self.assertEqual(s.isPerfectSquare(1), True)
