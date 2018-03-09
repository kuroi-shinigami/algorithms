from unittest import TestCase

from count_binary_substrings import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.countBinarySubstrings("00110011"), 6)

    def test_1(self):
        self.assertEqual(s.countBinarySubstrings("10101"), 4)
