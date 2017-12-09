#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from itertools import combinations


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # remove all too big numbers
        # nums = [x for x in nums if x <= target]  # What about 0?
        # not unsigned integers, Carl!
        for x, y in combinations(nums, 2):
            if x + y == target:
                # [3,3]: removing items from list and adding to shrtened list index of second item
                ix = nums.index(x)
                nums.pop(ix)
                return [ix, nums.index(y)+1]


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([14, 88, 134, 2, 7, 11, 15], 9))
