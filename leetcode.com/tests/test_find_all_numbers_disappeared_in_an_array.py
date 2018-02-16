from unittest import TestCase

from find_all_numbers_disappeared_in_an_array import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]), [5, 6])

    def test_1(self):
        self.assertEqual(s.findDisappearedNumbers([1, 1]), [2])

    def test_2(self):
        self.assertEqual(s.findDisappearedNumbers([1, 2]), [])

    def test_3(self):
        self.assertEqual(s.findDisappearedNumbers([1, 1, 2, 2]), [3, 4])
