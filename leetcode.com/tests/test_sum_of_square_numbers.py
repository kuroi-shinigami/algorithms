from unittest import TestCase

from sum_of_square_numbers import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.judgeSquareSum(5), True)

    def test_1(self):
        self.assertEqual(s.judgeSquareSum(3), False)

    def test_2(self):
        self.assertEqual(s.judgeSquareSum(4), True)

    def test_3(self):
        self.assertEqual(s.judgeSquareSum(1000000000), True)
