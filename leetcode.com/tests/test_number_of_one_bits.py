from unittest import TestCase


from number_of_one_bits import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.hammingWeight(5), 2)
