#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        threshhold = len(nums)/2

        # Hello, bad taste!
        if len(nums) == 1:
            return nums[0]

        d = dict()
        for i in nums:
            if i in d:
                d[i] += 1
                if d[i] > threshhold:
                    return i
            else:
                d[i] = 1
