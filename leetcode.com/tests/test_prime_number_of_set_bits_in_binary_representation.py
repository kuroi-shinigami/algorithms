from unittest import TestCase

from prime_number_of_set_bits_in_binary_representation import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.countPrimeSetBits(6, 10), 4)

    def test_1(self):
        self.assertEqual(s.countPrimeSetBits(10, 15), 5)

    def test_2(self):
        self.assertEqual(s.countPrimeSetBits(990, 1048), 28)
