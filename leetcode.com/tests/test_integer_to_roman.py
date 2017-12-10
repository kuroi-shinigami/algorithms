from unittest import TestCase


from integer_to_roman import Solution

s = Solution()


class TestSolution(TestCase):
    """"""
    def test_0(self):
        self.assertEqual(s.intToRoman(3), 'III')

    def test_1(self):
        self.assertEqual(s.intToRoman(5), 'V')

    def test_2(self):
        self.assertEqual(s.intToRoman(12), 'XII')

    def test_4(self):
        self.assertEqual(s.intToRoman(4), 'IV')

    def test_5(self):
        self.assertEqual(s.intToRoman(9), 'IX')

    def test_6(self):
        self.assertEqual(s.intToRoman(6), 'VI')

    def test_7(self):
        self.assertEqual(s.intToRoman(41), 'XLI')  # May be wrong

    def test_8(self):
        self.assertEqual(s.intToRoman(40), 'XL')

    def test_9(self):
        self.assertEqual(s.intToRoman(23), 'XXIII')

    def test_10(self):
        self.assertEqual(s.intToRoman(21), 'XXI')
