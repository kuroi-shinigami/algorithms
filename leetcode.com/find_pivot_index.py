#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # for i in range(len(nums)):
        #     if sum(nums[:i]) == sum(nums[i+1:]):
        #         return i
        # return -1

        # if not nums:
        #     return -1
        # p = [nums[0]]
        # for i in range(1, len(nums)):
        #     p.append(p[i-1] + nums[i])
        #
        # # print(p)
        # # print(nums)
        #
        # for i in range(len(nums)-1):
        #     # print(i, p[-1] - nums[i] - p[i])
        #     if p[i] == p[-1] - nums[i+1] - p[i]:
        #         return i+1
        # return -1

        if not nums:
            return -1
        p = [0]
        for i in range(len(nums)):
            p.append(p[i] + nums[i])

        # print(p)
        # print(nums)

        for i in range(len(nums)):
            # print(i, p[i], p[-1] - nums[i] - p[i])
            if p[i] == p[-1] - nums[i] - p[i]:
                return i
        return -1
