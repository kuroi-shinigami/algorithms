from unittest import TestCase

from excel_sheet_column_title import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.convertToTitle(1), "A")

    def test_1(self):
        self.assertEqual(s.convertToTitle(25), "Y")

    def test_2(self):
        self.assertEqual(s.convertToTitle(26), "Z")

    def test_3(self):
        self.assertEqual(s.convertToTitle(27), "AA")

    def test_4(self):
        self.assertEqual(s.convertToTitle(28), "AB")

    def test_5(self):
        self.assertEqual(s.convertToTitle(53), "BA")

    def test_6(self):
        self.assertEqual(s.convertToTitle(52), "AZ")

    def test_7(self):
        self.assertEqual(s.convertToTitle(701), "ZY")
