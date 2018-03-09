from unittest import TestCase


from find_the_difference import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.findTheDifference("abcd", "abcde"), "e")
