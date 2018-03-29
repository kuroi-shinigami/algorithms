#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        _nums1 = {}
        _nums2 = {}
        for _dict, _list in zip([_nums1, _nums2], [nums1, nums2]):
            for x in _list:
                if x not in _dict:
                    _dict[x] = 1
                else:
                    _dict[x] += 1
        small, large = (_nums1, _nums2) if len(_nums1) < len(_nums2) else (_nums2, _nums1)
        res = []
        for k in small:
            if k in large:
                count = small[k] if large[k] > small[k] else large[k]
                res += [k]*count
        return res
