#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        longest = 0
        current = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                current += 1
            else:
                if current > longest:
                    longest = current
                current = 1
        if current > longest:
            longest = current
        return longest
