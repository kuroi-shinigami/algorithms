#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1 += nums2
        nums1.sort()  # Python uses timsort. Doesn't it count?
        if len(nums1) % 2:
            return nums1[int(len(nums1) / 2 - 0.5)]
        else:
            ix = int(len(nums1) / 2)
            return (nums1[ix] + nums1[ix - 1]) / 2
