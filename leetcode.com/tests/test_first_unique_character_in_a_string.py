from unittest import TestCase


from first_unique_character_in_a_string import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.firstUniqChar("leetcode"), 0)

    def test_1(self):
        self.assertEqual(s.firstUniqChar("loveleetcode"), 2)
