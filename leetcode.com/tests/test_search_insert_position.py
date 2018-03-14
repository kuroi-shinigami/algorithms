from unittest import TestCase

from search_insert_position import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.searchInsert([1, 3, 5, 6], 5), 2)

    def test_1(self):
        self.assertEqual(s.searchInsert([1, 3, 5, 6], 2), 1)

    def test_2(self):
        self.assertEqual(s.searchInsert([1, 3, 5, 6], 7), 4)

    def test_3(self):
        self.assertEqual(s.searchInsert([1, 3, 5, 6], 0), 0)

    def test_4(self):
        self.assertEqual(s.searchInsert([1, 3], 2), 1)
