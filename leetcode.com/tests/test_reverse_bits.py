from unittest import TestCase


from reverse_bits import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.reverseBits(43261596), 964176192)

    def test_1(self):
        self.assertEqual(s.reverseBits(2147483648), 1)
