#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = [-1, -1]
        if not nums:
            return res
        start = 0
        end = len(nums)
        while start != end:
            idx = (start + end) // 2
            value = nums[idx]
            if value == target:
                break
            elif value < target:
                end = idx
            else:
                start = idx + 1
        # ToDo: when we found 1-st idx with target use binary search either
        res = set()
        for i in range(idx, len(nums)):
            if nums[i] == target:
                res.add(i)
        for i in range(idx, -1, -1):
            if nums[i] == target:
                res.add(i)
        if res:
            return [min(res), max(res)]
        else:
            return [-1, -1]
