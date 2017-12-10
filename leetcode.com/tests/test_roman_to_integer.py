from unittest import TestCase


from roman_to_integer import Solution

s = Solution()


class TestSolution(TestCase):
    """"""
    def test_0(self):
        self.assertEqual(s.romanToInt('III'), 3)

    def test_1(self):
        self.assertEqual(s.romanToInt('V'), 5)

    def test_2(self):
        self.assertEqual(s.romanToInt('XII'), 12)

    def test_3(self):
        self.assertEqual(s.romanToInt('IV'), 4)
