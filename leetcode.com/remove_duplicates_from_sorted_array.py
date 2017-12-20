#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Are you f*cking kidding me?
        # return len(set(nums))
        ix = 0
        if nums:
            for i in range(1, len(nums)):
                if nums[ix] != nums[i]:
                    ix += 1
                    nums[ix] = nums[i]
            ix += 1
        return ix
