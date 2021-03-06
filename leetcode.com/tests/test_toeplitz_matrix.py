from unittest import TestCase

from toeplitz_matrix import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.isToeplitzMatrix([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]), True)

    def test_1(self):
        self.assertEqual(s.isToeplitzMatrix([[1, 2], [2, 2]]), False)

    def test_2(self):
        self.assertEqual(s.isToeplitzMatrix([[36, 59, 71, 15, 26, 82, 87],
                                             [56, 36, 59, 71, 15, 26, 82],
                                             [15, 0, 36, 59, 71, 15, 26]]), False)

    def test_3(self):
        self.assertEqual(s.isToeplitzMatrix([[27, 0, 62, 57, 23, 4, 28, 54, 63, 1, 59, 92, 50, 3],
                                             [59, 27, 0, 62, 57, 23, 4, 28, 54, 63, 1, 59, 92, 50],
                                             [59, 59, 27, 0, 62, 57, 23, 4, 28, 54, 63, 1, 59, 92],
                                             [67, 59, 59, 27, 0, 62, 57, 23, 4, 28, 54, 63, 1, 59],
                                             [45, 67, 59, 59, 27, 0, 62, 57, 23, 4, 28, 54, 63, 1],
                                             [31, 45, 67, 59, 59, 27, 0, 62, 57, 23, 4, 28, 54, 63],
                                             [92, 31, 45, 67, 59, 59, 27, 0, 62, 57, 23, 4, 28, 54],
                                             [81, 92, 31, 45, 67, 59, 59, 27, 0, 62, 57, 23, 4, 28],
                                             [10, 81, 92, 31, 45, 67, 59, 59, 27, 0, 62, 57, 23, 4],
                                             [61, 10, 81, 92, 31, 45, 67, 59, 59, 27, 0, 62, 57, 23],
                                             [22, 61, 10, 81, 92, 31, 45, 67, 59, 59, 27, 0, 62, 57],
                                             [67, 22, 61, 10, 81, 92, 31, 45, 67, 59, 59, 27, 0, 62],
                                             [5, 67, 22, 61, 10, 81, 92, 31, 45, 67, 59, 59, 27, 0],
                                             [11, 5, 67, 22, 61, 10, 81, 92, 31, 45, 67, 59, 59, 27],
                                             [38, 11, 5, 67, 22, 61, 10, 81, 92, 31, 45, 67, 59, 59],
                                             [17, 38, 11, 5, 67, 22, 61, 10, 81, 92, 31, 45, 67, 59],
                                             [77, 17, 38, 11, 5, 67, 22, 61, 10, 81, 92, 31, 45, 67],
                                             [37, 77, 17, 38, 11, 5, 67, 22, 61, 10, 81, 92, 31, 45],
                                             [87, 37, 77, 17, 38, 11, 5, 67, 22, 61, 10, 81, 92, 31],
                                             [43, 87, 37, 77, 17, 38, 11, 5, 67, 22, 61, 10, 81, 92]]), True)
