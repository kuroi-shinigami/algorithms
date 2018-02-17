from unittest import TestCase

from ransom_note import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.canConstruct("a", "b"), False)

    def test_1(self):
        self.assertEqual(s.canConstruct("aa", "ab"), False)

    def test_2(self):
        self.assertEqual(s.canConstruct("aa", "aab"), True)

    # def test_(self):
    #     self.assertEqual(s.canConstruct(), )
