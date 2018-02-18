from unittest import TestCase

from letter_case_permutation import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(set(s.letterCasePermutation("a1b2")), {"a1b2", "a1B2", "A1b2", "A1B2"})

    def test_1(self):
        self.assertEqual(set(s.letterCasePermutation("3z4")), {"3z4", "3Z4"})

    def test_2(self):
        self.assertEqual(set(s.letterCasePermutation("12345")), {"12345"})

    def test_3(self):
        self.assertEqual(set(s.letterCasePermutation("")), {""})
