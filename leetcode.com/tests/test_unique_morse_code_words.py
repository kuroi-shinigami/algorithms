from unittest import TestCase

from unique_morse_code_words import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]), 2)
