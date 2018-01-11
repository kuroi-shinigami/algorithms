from unittest import TestCase


from median_of_two_sorted_arrays import Solution

s = Solution()


class TestSolution(TestCase):

    def test_0(self):
        self.assertEqual(s.findMedianSortedArrays([1, 1], [1, 2]), 1.0)

    def test_1(self):
        self.assertEqual(s.findMedianSortedArrays([1, 2], [3, 4]), 2.5)

    def test_2(self):
        self.assertEqual(s.findMedianSortedArrays([1, 3], [2]), 2.0)

    def test_3(self):
        self.assertEqual(s.findMedianSortedArrays([1], []), 1.0)

    def test_4(self):
        self.assertEqual(s.findMedianSortedArrays([4, 5, 6, 8, 9], []), 6.0)

    def test_5(self):
        self.assertEqual(s.findMedianSortedArrays([1, 1, 1, 1], [2, 2, 2, 2]), 1.5)

    def test_6(self):
        self.assertEqual(s.findMedianSortedArrays([1, 1, 1, 1], [2, 2, 2, 2, 2, 2]), 2)

    def test_7(self):
        self.assertEqual(s.findMedianSortedArrays([1, 1, 1], [2, 2, 2, 2]), 2)
