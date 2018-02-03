from unittest import TestCase

from nim_game import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.canWinNim(4), False)
