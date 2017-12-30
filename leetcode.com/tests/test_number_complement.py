from unittest import TestCase


from number_complement import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.findComplement(1), 0)

    def test_1(self):
        self.assertEqual(s.findComplement(5), 2)
