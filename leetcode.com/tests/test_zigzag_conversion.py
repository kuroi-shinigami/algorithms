from unittest import TestCase


from zigzag_conversion import Solution

s = Solution()


class TestSolution(TestCase):
    """"""
    def test_0(self):
        self.assertEqual(s.convert("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")

    def test_1(self):
        self.assertEqual(s.convert("AB", 1), "AB")

    def test_2(self):
        self.assertEqual(s.convert("ABC", 2), "ACB")
