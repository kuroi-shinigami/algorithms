from unittest import TestCase

from ugly_number import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.isUgly(1), True)

    def test_1(self):
        self.assertEqual(s.isUgly(6), True)

    def test_2(self):
        self.assertEqual(s.isUgly(8), True)

    def test_3(self):
        self.assertEqual(s.isUgly(14), False)

    def test_4(self):
        self.assertEqual(s.isUgly(0), False)

