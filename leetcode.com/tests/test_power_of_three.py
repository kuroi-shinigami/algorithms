from unittest import TestCase

from power_of_three import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.isPowerOfThree(0), False)

    def test_1(self):
        self.assertEqual(s.isPowerOfThree(1), True)

    def test_2(self):
        self.assertEqual(s.isPowerOfThree(3), True)

    def test_3(self):
        self.assertEqual(s.isPowerOfThree(9), True)

    def test_4(self):
        self.assertEqual(s.isPowerOfThree(5), False)

    def test_5(self):
        self.assertEqual(s.isPowerOfThree(243), True)
