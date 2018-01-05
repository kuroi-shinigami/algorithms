from unittest import TestCase


from keyboard_row import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.findWords(["Hello", "Alaska", "Dad", "Peace"]), ["Alaska", "Dad"])
