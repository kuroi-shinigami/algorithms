from unittest import TestCase

from minimum_index_sum_of_two_lists import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"],  ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]), ["Shogun"])

    def test_1(self):
        self.assertEqual(s.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"],  ["KFC", "Shogun", "Burger King"]), ["Shogun"])
