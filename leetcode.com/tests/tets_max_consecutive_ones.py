from unittest import TestCase


from max_consecutive_ones import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]), 3)
