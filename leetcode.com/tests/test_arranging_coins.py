from unittest import TestCase

from arranging_coins import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.arrangeCoins(5), 2)

    def test_1(self):
        self.assertEqual(s.arrangeCoins(8), 3)

    def test_2(self):
        self.assertEqual(s.arrangeCoins(1), 1)

    def test_3(self):
        self.assertEqual(s.arrangeCoins(0), 0)

    def test_4(self):
        self.assertEqual(s.arrangeCoins(3), 2)
