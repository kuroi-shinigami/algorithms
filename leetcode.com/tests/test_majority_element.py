from unittest import TestCase

from majority_element import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.majorityElement([0, 1, 1, 1]), 1)

    def test_1(self):
        self.assertEqual(s.majorityElement([1]), 1)
