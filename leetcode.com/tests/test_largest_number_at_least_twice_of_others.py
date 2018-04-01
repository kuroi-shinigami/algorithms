from unittest import TestCase

from largest_number_at_least_twice_of_others import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.dominantIndex([3, 6, 1, 0]), 1)

    def test_1(self):
        self.assertEqual(s.dominantIndex([1, 2, 3, 4]), -1)

    def test_2(self):
        self.assertEqual(s.dominantIndex([1]), 0)
