from unittest import TestCase

from degree_of_an_array import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.findShortestSubArray([1, 2, 2, 3, 1]), 2)

    def test_1(self):
        self.assertEqual(s.findShortestSubArray([1, 2, 2, 3, 1, 4, 2]), 6)
