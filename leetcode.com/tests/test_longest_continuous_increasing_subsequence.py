from unittest import TestCase

from longest_continuous_increasing_subsequence import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.findLengthOfLCIS([1, 3, 5, 4, 7]), 3)

    def test_1(self):
        self.assertEqual(s.findLengthOfLCIS([2, 2, 2, 2, 2]), 1)

    def test_2(self):
        self.assertEqual(s.findLengthOfLCIS([1, 3, 5, 4, 2, 3, 4, 5]), 4)
