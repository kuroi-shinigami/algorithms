#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = -1
        _max = max(nums)
        _idx = nums.index(_max)
        # nums.pop(_idx)
        del nums[_idx]
        if len(nums) == 0:
            return 0
        _target = max(nums)
        if _target*2 <= _max:
            return _idx
        return res
