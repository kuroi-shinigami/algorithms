from unittest import TestCase


from hamming_distance import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.hammingDistance(1, 0), 1)

    def test_1(self):
        self.assertEqual(s.hammingDistance(1, 4), 2)
