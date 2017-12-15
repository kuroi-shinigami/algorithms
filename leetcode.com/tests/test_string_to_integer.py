from unittest import TestCase


from string_to_integer import Solution

s = Solution()


class TestSolution(TestCase):
    """"""
    def test_0(self):
        self.assertEqual(s.myAtoi(''), 0)

    def test_1(self):
        self.assertEqual(s.myAtoi('  -0012a42'), -12)

    def test_2(self):
        self.assertEqual(s.myAtoi('-+1'), 0)

    def test_3(self):
        self.assertEqual(s.myAtoi("2147483648"), 2147483647)

    def test_4(self):
        self.assertEqual(s.myAtoi("   - 321"), 0)

    def test_5(self):
        self.assertEqual(s.myAtoi("   +0 123"), 0)

    def test_6(self):
        self.assertEqual(s.myAtoi("+1"), 1)

    def test_7(self):
        self.assertEqual(s.myAtoi("     +004500"), 4500)

    def test_8(self):
        self.assertEqual(s.myAtoi("  -0 451"), 0)
