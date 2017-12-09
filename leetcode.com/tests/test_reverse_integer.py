from unittest import TestCase


from reverse_integer import Solution

s = Solution()


class TestSolution(TestCase):
    """"""
    def test_1(self):
        self.assertEqual(s.reverse(123), 321)

    def test_2(self):
        self.assertEqual(s.reverse(-123), -321)

    def test_3(self):
        self.assertEqual(s.reverse(120), 21)

    def test_4(self):
        self.assertEqual(s.reverse(1534236469), 0)

    def test_5(self):
        self.assertEqual(s.reverse(900000), 9)

    def test_6(self):
        self.assertEqual(s.reverse(1563847412), 0)
