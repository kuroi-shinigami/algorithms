from unittest import TestCase

from happy_number import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.isHappy(19), True)

    def test_1(self):
        self.assertEqual(s.isHappy(2), False)
