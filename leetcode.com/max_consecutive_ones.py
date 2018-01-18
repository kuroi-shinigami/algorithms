#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_ones = 0
        counter = 0
        for x in nums:
            if x:
                counter += 1
            else:
                if counter > max_ones:
                    max_ones = counter
                counter = 0
        if counter > max_ones:
            max_ones = counter
        return max_ones
