from unittest import TestCase

from missing_number import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.missingNumber([3, 0, 1]), 2)

    def test_1(self):
        self.assertEqual(s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]), 8)

    def test_2(self):
        self.assertEqual(s.missingNumber([0, 1]), 2)

    def test_3(self):
        self.assertEqual(s.missingNumber([1]), 0)

    def test_5(self):
        self.assertEqual(s.missingNumber([0]), 1)

    def test_6(self):
        self.assertEqual(s.missingNumber([1, 2]), 0)
