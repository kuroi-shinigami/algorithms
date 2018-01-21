from unittest import TestCase

from array_partition_I import Solution

s = Solution()


class TestSolution(TestCase):

    def test_0(self):
        self.assertEqual(s.arrayPairSum([1, 4, 3, 2]), 4)
