from unittest import TestCase

from length_of_last_word import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.lengthOfLastWord("Hello World"), 5)

    def test_1(self):
        self.assertEqual(s.lengthOfLastWord("a "), 1)

    def test_2(self):
        self.assertEqual(s.lengthOfLastWord(""), 0)
