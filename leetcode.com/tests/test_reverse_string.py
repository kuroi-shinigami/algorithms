from unittest import TestCase


from reverse_string import Solution

s = Solution()


class TestSolution(TestCase):
    """"""
    def test_0(self):
        self.assertEqual(s.reverseString('hello'), 'olleh')
