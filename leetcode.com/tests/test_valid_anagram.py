from unittest import TestCase

from valid_anagram import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.isAnagram("anagram", "nagaram"), True)

    def test_1(self):
        self.assertEqual(s.isAnagram("rat", "car"), False)

    def test_2(self):
        self.assertEqual(s.isAnagram("aa", "a"), False)
