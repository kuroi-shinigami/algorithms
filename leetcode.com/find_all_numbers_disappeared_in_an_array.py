#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        if nums:
            top = len(nums) + 1
            nums = set(nums)

            for i in range(1, top):
                if i not in nums:
                    res.append(i)
        return res
