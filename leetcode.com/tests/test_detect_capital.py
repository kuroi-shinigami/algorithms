from unittest import TestCase

from detect_capital import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.detectCapitalUse("USA"), True)

    def test_1(self):
        self.assertEqual(s.detectCapitalUse("FlaG"), False)

    def test_2(self):
        self.assertEqual(s.detectCapitalUse("leetcode"), True)

    def test_3(self):
        self.assertEqual(s.detectCapitalUse("Google"), True)
