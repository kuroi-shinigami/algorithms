from unittest import TestCase


from valid_parentheses import Solution

s = Solution()


class TestSolution(TestCase):

    def test_0(self):
        self.assertEqual(s.isValid('()[]{}'), True)

    def test_1(self):
        self.assertEqual(s.isValid('(]'), False)

    def test_2(self):
        self.assertEqual(s.isValid('([)]'), False)

    def test_3(self):
        self.assertEqual(s.isValid('}'), False)

    def test_4(self):
        self.assertEqual(s.isValid('()'), True)
