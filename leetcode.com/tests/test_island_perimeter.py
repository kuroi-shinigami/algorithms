from unittest import TestCase

from island_perimeter import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]), 16)

    def test_1(self):
        self.assertEqual(s.islandPerimeter([[1], [0]]), 4)
