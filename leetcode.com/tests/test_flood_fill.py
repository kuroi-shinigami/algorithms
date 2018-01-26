from unittest import TestCase

from flood_fill import Solution

s = Solution()


class TestSolution(TestCase):

    def test_0(self):
        self.assertEqual(s.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2), [[2, 2, 2], [2, 2, 0], [2, 0, 1]])

    def test_1(self):
        self.assertEqual(s.floodFill([[0, 0, 0], [0, 1, 1]], 1, 1, 1), [[0, 0, 0], [0, 1, 1]])
