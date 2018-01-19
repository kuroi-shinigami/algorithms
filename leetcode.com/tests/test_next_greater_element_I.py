from unittest import TestCase

from next_greater_element_I import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]), [-1, 3, -1])

    def test_1(self):
        self.assertEqual(s.nextGreaterElement([2, 4], [1, 2, 3, 4]), [3, -1])
