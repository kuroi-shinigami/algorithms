from unittest import TestCase

from plus_one import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.plusOne([0]), [1])

    def test_1(self):
        self.assertEqual(s.plusOne([9]), [1, 0])

    def test_2(self):
        self.assertEqual(s.plusOne([1, 9]), [2, 0])
