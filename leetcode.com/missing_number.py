#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 1:
                return nums[i] - 1
        return nums[-1] + 1 if not nums[0] else 0
