from unittest import TestCase


from reverse_words_in_a_string_III import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.reverseWords("Let's take LeetCode contest"), "s'teL ekat edoCteeL tsetnoc")
