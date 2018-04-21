from unittest import TestCase

from search_for_a_range import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.searchRange([5, 7, 7, 8, 8, 10], 8), [3, 4])

    def test_1(self):
        self.assertEqual(s.searchRange([5, 7, 7, 8, 8, 10], 6), [-1, -1])

    def test_2(self):
        self.assertEqual(s.searchRange([1], 1), [0, 0])

    def test_3(self):
        self.assertEqual(s.searchRange([2, 2], 2), [0, 1])

    def test_4(self):
        self.assertEqual(s.searchRange([1, 3], 1), [0, 0])
