from unittest import TestCase


from longest_common_prefix import Solution

s = Solution()


class TestSolution(TestCase):

    def test_0(self):
        self.assertEqual(s.longestCommonPrefix(['aaaac', 'aaaceb', 'aaaad', 'aaeaaaaaa']), 'aa')

    def test_1(self):
        self.assertEqual(s.longestCommonPrefix([]), '')

    def test_2(self):
        self.assertEqual(s.longestCommonPrefix(['a']), 'a')
