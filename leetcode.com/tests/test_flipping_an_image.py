from unittest import TestCase

from flipping_an_image import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]), [[1, 0, 0], [0, 1, 0], [1, 1, 1]])

    def test_1(self):
        self.assertEqual(s.flipAndInvertImage([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]),
                         [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]])
