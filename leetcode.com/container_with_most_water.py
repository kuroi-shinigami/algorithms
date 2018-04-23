#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        i = 0
        j = len(height) - 1
        while i != j:
            l = height[i]
            r = height[j]
            w = j - i
            if l < r:
                i += 1
                m = w * l
            else:
                j -= 1
                m = w * r
            if m > res:
                res = m
        return res
