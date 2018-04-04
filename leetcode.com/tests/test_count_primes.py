from unittest import TestCase

from count_primes import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.countPrimes(3), 1)

    def test_1(self):
        self.assertEqual(s.countPrimes(5), 2)

    def test_2(self):
        self.assertEqual(s.countPrimes(0), 0)

    def test_3(self):
        self.assertEqual(s.countPrimes(2), 0)

    def test_4(self):
        self.assertEqual(s.countPrimes(10), 4)

    def test_5(self):
        self.assertEqual(s.countPrimes(499979), 41537)

    def test_6(self):
        self.assertEqual(s.countPrimes(999983), 78497)
