#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = {}
        for x in nums:
            if x not in seen:
                seen[x] = 1
            else:
                seen[x] += 1
        for x in seen:
            if seen[x] == 1:
                return x
