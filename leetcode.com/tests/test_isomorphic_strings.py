from unittest import TestCase

from isomorphic_strings import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.isIsomorphic("egg", "add"), True)

    def test_1(self):
        self.assertEqual(s.isIsomorphic("foo", "bar"), False)

    def test_2(self):
        self.assertEqual(s.isIsomorphic("paper", "title"), True)
