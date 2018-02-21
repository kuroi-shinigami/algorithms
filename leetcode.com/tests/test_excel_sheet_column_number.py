from unittest import TestCase

from excel_sheet_column_number import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.titleToNumber("A"), 1)

    def test_1(self):
        self.assertEqual(s.titleToNumber("Z"), 26)

    def test_2(self):
        self.assertEqual(s.titleToNumber("AA"), 27)

    def test_3(self):
        self.assertEqual(s.titleToNumber("AB"), 28)

    def test_4(self):
        self.assertEqual(s.titleToNumber("BA"), 53)
