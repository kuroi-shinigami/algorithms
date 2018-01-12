from unittest import TestCase


from single_number import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.singleNumber([-1]), -1)
