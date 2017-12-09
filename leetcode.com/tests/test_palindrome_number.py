from unittest import TestCase


from palindrome_number import Solution

s = Solution()


class TestSolution(TestCase):
    """"""
    def test_0(self):
        self.assertEqual(s.isPalindrome(131), True)

    def test_1(self):
        self.assertEqual(s.isPalindrome(1488), False)

    def test_2(self):
        self.assertEqual(s.isPalindrome(1441), True)

    def test_3(self):
        self.assertEqual(s.isPalindrome(0), True)

    def test_4(self):
        self.assertEqual(s.isPalindrome(-2147483648), False)

    def test_5(self):
        self.assertEqual(s.isPalindrome(-132231), False)  # Was True. Looks like a negative number can't be palindrom

    def test_6(self):
        self.assertEqual(s.isPalindrome(-2147447412), False)
