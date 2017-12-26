#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        ix = 0
        if nums:
            for i in range(0, len(nums)):
                if nums[i] != val:
                    nums[ix] = nums[i]
                    ix += 1
        return ix
