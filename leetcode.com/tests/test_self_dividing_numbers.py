from unittest import TestCase


from self_dividing_numbers import Solution

s = Solution()


class TestSolution(TestCase):
    """"""
    def test_(self):
        self.assertEqual(s.selfDividingNumbers(1, 22), [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22])
