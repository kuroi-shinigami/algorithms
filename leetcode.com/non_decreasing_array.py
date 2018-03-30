#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) > 1:
            _raptures = 0
            if nums[0] > nums[1]:
                _raptures += 1
                nums[0] = nums[1]
            _n = len(nums)
            for i in range(1, _n):
                if nums[i-1] > nums[i]:
                    if i-2 >= 0:
                        if nums[i-2] <= nums[i]:
                            nums[i-1] = nums[i-2]
                        else:
                            nums[i] = nums[i-1]
                    _raptures += 1
                if _raptures > 1:
                    return False
        return True
