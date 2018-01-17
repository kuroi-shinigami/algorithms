#!/usr/bin/env python
# -*- coding: UTF-8 -*-


# from itertools import combinations


class Solution:
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Too slow. 283ms at test_0
        # return sum([bin(x ^ y).count("1") for x, y in combinations(nums, 2)])

        # Even more slow. 310 ms at test_0
        # res = 0
        # n = len(nums)
        # for i in range(0, n):
        #     t = nums[i]
        #     for j in range(i, n):
        #         res += bin(t ^ nums[j]).count("1")
        # return res

        hash_table = {}
        res = 0
        for i in range(len(nums)):
            _row = "{:b}".format(nums[i])[::-1]
            for j in range(len(_row)):
                if _row[j] == "1":
                    if j in hash_table:
                        hash_table[j] += 1
                    else:
                        hash_table[j] = 1
        for j in hash_table.values():
            res += j * (len(nums) - j)
        return res
