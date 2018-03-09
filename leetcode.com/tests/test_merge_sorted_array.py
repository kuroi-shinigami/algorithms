from unittest import TestCase


from merge_sorted_array import Solution

s = Solution()


class TestSolution(TestCase):
    """"""
    def test_0(self):
        self.assertEqual(s.merge([0], 0, [1], 1), [0, 1])

    def test_1(self):
        self.assertEqual(s.merge([1], 1, [], 0), [1])
