#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums_dict = {x: i for (i, x) in enumerate(nums2)}
        res = []
        for x in nums1:
            ix = nums_dict.get(x, 0)
            for y in nums2[ix:]:
                if y > x:
                    res.append(y)
                    break
            else:
                res.append(-1)
        return res
