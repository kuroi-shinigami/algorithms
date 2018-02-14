from unittest import TestCase

from binary_number_with_alternating_bits import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.hasAlternatingBits(5), True)

    def test_1(self):
        self.assertEqual(s.hasAlternatingBits(7), False)

    def test_2(self):
        self.assertEqual(s.hasAlternatingBits(11), False)

    def test_3(self):
        self.assertEqual(s.hasAlternatingBits(10), True)
