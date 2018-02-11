#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        counts = {}
        longest = 0
        for i in range(len(nums)):
            if nums[i] in counts:
                counts[nums[i]] += 1
            else:
                counts[nums[i]] = 1
        _counts = list(sorted(counts))
        for i in range(1, len(_counts)):
            if _counts[i] - _counts[i-1] == 1:
                s = counts[_counts[i]] + counts[_counts[i-1]]
                print(s)
                if s > longest:
                    longest = s
        return longest
