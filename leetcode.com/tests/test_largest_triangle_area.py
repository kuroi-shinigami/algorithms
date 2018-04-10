from unittest import TestCase

from largest_triangle_area import Solution

s = Solution()
epsilon = 10 ** -6


class TestSolution(TestCase):
    """"""

    def test_0(self):
        answer = 2.0
        guess = s.largestTriangleArea([[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]])
        self.assertTrue(abs(answer - guess) < epsilon)
