from unittest import TestCase

from reverse_vowels_of_a_string import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.reverseVowels("hello"), "holle")

    def test_1(self):
        self.assertEqual(s.reverseVowels("leetcode"), "leotcede")

    def test_2(self):
        self.assertEqual(s.reverseVowels("aA"), "Aa")
