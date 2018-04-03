from unittest import TestCase

from power_of_two import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.isPowerOfTwo(2), True)

    def test_1(self):
        self.assertEqual(s.isPowerOfTwo(4), True)

    def test_2(self):
        self.assertEqual(s.isPowerOfTwo(5), False)

    def test_3(self):
        self.assertEqual(s.isPowerOfTwo(1), True)

    def test_4(self):
        self.assertEqual(s.isPowerOfTwo(6), False)

    def test_5(self):
        self.assertEqual(s.isPowerOfTwo(-16), False)
