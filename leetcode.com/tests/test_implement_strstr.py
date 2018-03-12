from unittest import TestCase

from implement_strstr import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.strStr("hello", "ll"), 2)

    def test_1(self):
        self.assertEqual(s.strStr("aaaaa", "bba"), -1)

    def test_2(self):
        self.assertEqual(s.strStr("", ""), 0)
