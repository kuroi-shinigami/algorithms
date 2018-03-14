#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in set(nums):
            return nums.index(target)
        else:
            _min = 0
            _max = len(nums)
            if target < nums[0]:
                return 0
            if target > nums[-1]:
                return len(nums)

            while _min != _max:
                cmp = (_min + _max) // 2
                if target < nums[cmp]:
                    _max = cmp
                else:
                    _min = cmp + 1
            return _min
