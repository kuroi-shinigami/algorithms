from unittest import TestCase

from most_common_word import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]), "ball")
