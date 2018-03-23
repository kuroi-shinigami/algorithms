from unittest import TestCase

from sqrt_x import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.mySqrt(4), 2)

    def test_1(self):
        self.assertEqual(s.mySqrt(8), 2)

    def test_2(self):
        self.assertEqual(s.mySqrt(1), 1)

    def test_3(self):
        self.assertEqual(s.mySqrt(1595689904), 39946)

    def test_4(self):
        self.assertEqual(s.mySqrt(808909662), 28441)
