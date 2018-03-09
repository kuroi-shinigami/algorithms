from unittest import TestCase


from longest_uncommon_subsequence_I import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.findLUSlength('aba', 'cdc'), 3)

    def test_1(self):
        self.assertEqual(s.findLUSlength("aaa", "aaa"), -1)

    def test_2(self):
        self.assertEqual(s.findLUSlength("aefawfawfawfaw", "aefawfeawfwafwaef"), 17)

    def test_3(self):
        self.assertEqual(s.findLUSlength("", ""), -1)
