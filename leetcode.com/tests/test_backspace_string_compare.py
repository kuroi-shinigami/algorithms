from unittest import TestCase

from backspace_string_compare import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.backspaceCompare("ab#c", "ab#c"), True)

    def test_1(self):
        self.assertEqual(s.backspaceCompare("ab##", "c#d#"), True)

    def test_2(self):
        self.assertEqual(s.backspaceCompare("a##c", "#a#c"), True)

    def test_3(self):
        self.assertEqual(s.backspaceCompare("a#c", "b"), False)

    def test_4(self):
        self.assertEqual(s.backspaceCompare("ac#", "a"), True)

    def test_5(self):
        self.assertEqual(s.backspaceCompare("cv##pzk###t##m#p#qb##o##kmenj##zto###", "cv##pzk##b##hmf###t##m#p#qb##r#n#o##kmenj##zto###"), True)
