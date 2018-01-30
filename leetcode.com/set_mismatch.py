#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Too slow, 588 ms on test_6
        #############################
        # nums.sort()
        # missing = None
        # repeated = None
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i - 1]:
        #         repeated = nums[i]
        #     # print(i, i in nums)
        #     if i not in nums:
        #         missing = i
        # if not missing:
        #     missing = nums[-1]+1
        # return [repeated, missing]
        repeated = None
        s = set()
        for x in nums:
            if x in s:
                repeated = x
            else:
                s.add(x)
        for i in range(0, len(s)):
            if i+1 not in s:
                missing = i+1
                break
        else:
            missing = max(s) + 1
        return [repeated, missing]
