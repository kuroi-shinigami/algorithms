from unittest import TestCase

from remove_element import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.removeElement([3, 2, 2, 3], 2), 2)

    def test_1(self):
        self.assertEqual(s.removeElement([3, 2, 2, 3], 3), 2)
