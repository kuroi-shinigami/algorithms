from unittest import TestCase

from intersection_of_two_arrays import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.intersection([1, 2, 2, 1], [2, 2]), [2])
