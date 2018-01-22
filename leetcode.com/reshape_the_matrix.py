#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r*c == len(nums) * len(nums[0]):
            res = []
            _res = []
            counter = 0
            for _row in nums:
                for d in _row:
                    _res.append(d)
                    counter += 1
                    if counter == c:
                        res.append(_res)
                        _res = []
                        counter = 0
            return res
        return nums