from unittest import TestCase


from perfect_number import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.checkPerfectNumber(28), True)

    def test_1(self):
        self.assertEqual(s.checkPerfectNumber(20996011), False)

    def test_2(self):
        self.assertEqual(s.checkPerfectNumber(99999991), False)
