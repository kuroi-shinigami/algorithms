from unittest import TestCase


from fizz_buzz import Solution

s = Solution()


class TestSolution(TestCase):
    """"""
    def test_0(self):
        self.assertEqual(s.fizzBuzz(15), ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz",
                                          "13", "14", "FizzBuzz"])
