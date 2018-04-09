from unittest import TestCase

from rotate_string import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.rotateString('abcde', 'cdeab'), True)

    def test_1(self):
        self.assertEqual(s.rotateString('abcde', 'abced'), False)
