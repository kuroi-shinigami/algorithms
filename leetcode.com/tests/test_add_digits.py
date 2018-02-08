from unittest import TestCase

from add_digits import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.addDigits(38), 2)

    def test_1(self):
        self.assertEqual(s.addDigits(0), 0)

    def test_2(self):
        self.assertEqual(s.addDigits(10), 1)
