#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        degrees = {}
        for x in nums:
            if x not in degrees:
                degrees[x] = 1
            else:
                degrees[x] += 1
        degree = max(degrees.values())
        target_nums = set([x for x in degrees if degrees[x] == degree])
        print(target_nums)
        print("Searching the shortest subarray")
        # Idea - just search for target nums in array and calculate subarray's
        # length from border indices. So we should get some like O(N) but it
        # depends. If array have many elements with same degree it should be worse.
        borders = {}
        for i, x in enumerate(nums):
            if x in target_nums:
                if x in borders:
                    borders[x].append(i)
                else:
                    borders[x] = [i]
        # +1 is for indices starts with 0
        return min([v[-1] - v[0] + 1 for v in borders.values()])
