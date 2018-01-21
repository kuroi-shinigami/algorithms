#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum([min(nums[i], nums[i+1]) for i in range(0, len(nums), 2)])
