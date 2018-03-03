from unittest import TestCase

from valid_palindrome import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.isPalindrome(''), True)

    def test_1(self):
        self.assertEqual(s.isPalindrome("A man, a plan, a canal: Panama"), True)

    def test_2(self):
        self.assertEqual(s.isPalindrome("race a car"), False)

    def test_3(self):
        self.assertEqual(s.isPalindrome("0P"), False)
