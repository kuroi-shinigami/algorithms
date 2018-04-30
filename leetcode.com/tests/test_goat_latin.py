from unittest import TestCase

from goat_latin import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.toGoatLatin("I speak Goat Latin"), "Imaa peaksmaaa oatGmaaaa atinLmaaaaa")

    def test_1(self):
        self.assertEqual(s.toGoatLatin("The quick brown fox jumped over the lazy dog"), "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa")
