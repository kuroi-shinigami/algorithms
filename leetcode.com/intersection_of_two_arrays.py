#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = set(nums1)
        nums2 = set(nums2)
        long, short = (nums1, nums2) if (len(nums1) > len(nums2)) else (nums2, nums1)
        res = []
        for x in short:
            if x in long:
                res.append(x)
        return res
