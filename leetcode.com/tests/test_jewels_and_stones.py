from unittest import TestCase

from jewels_and_stones import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.numJewelsInStones("aA", "aAAbbbb"), 3)

    def test_1(self):
        self.assertEqual(s.numJewelsInStones('z', "ZZ"), 0)
