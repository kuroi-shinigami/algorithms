from unittest import TestCase


from reverse_string_II import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.reverseStr("abcdefg", 2), "bacdfeg")
