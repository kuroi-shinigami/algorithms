from unittest import TestCase

from word_pattern import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.wordPattern("abba", "dog cat cat dog"), True)

    def test_1(self):
        self.assertEqual(s.wordPattern("abba", "dog cat cat fish"), False)

    def test_2(self):
        self.assertEqual(s.wordPattern("aaaa", "dog cat cat dog"), False)

    def test_3(self):
        self.assertEqual(s.wordPattern("abba", "dog dog dog dog"), False)

    def test_4(self):
        self.assertEqual(s.wordPattern("jquery", "jquery"), False)

    # def test_(self):
    #     self.assertEqual(s.wordPattern(), )
