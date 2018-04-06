from unittest import TestCase

from power_of_four import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_1(self):
        self.assertEqual(s.isPowerOfFour(1), True)

    def test_2(self):
        self.assertEqual(s.isPowerOfFour(4), True)

    def test_3(self):
        self.assertEqual(s.isPowerOfFour(8), False)

    def test_4(self):
        self.assertEqual(s.isPowerOfFour(5), False)

    def test_5(self):
        self.assertEqual(s.isPowerOfFour(16), True)

    def test_6(self):
        self.assertEqual(s.isPowerOfFour(0), False)
