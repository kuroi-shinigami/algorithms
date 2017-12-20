from unittest import TestCase


from remove_duplicates_from_sorted_array import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.removeDuplicates([1, 1, 2]), 2)

    def test_1(self):
        self.assertEqual(s.removeDuplicates([1, 1, 1]), 1)

    def test_2(self):
        self.assertEqual(s.removeDuplicates([]), 0)
