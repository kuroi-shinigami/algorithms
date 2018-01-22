from unittest import TestCase

from reshape_the_matrix import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.matrixReshape([[1, 2], [3, 4]], 2, 4), [[1, 2], [3, 4]])

    def test_1(self):
        self.assertEqual(s.matrixReshape([[1, 2], [3, 4]], 1, 4), [[1, 2, 3, 4]])
