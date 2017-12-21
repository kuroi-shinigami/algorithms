#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero_count = 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                zero_count += 1
        i = 0
        while i < len(nums)-zero_count:
            if nums[i] == 0:
                # Shift all [i+1:len(nums)-zero_count]
                for ix in range(i+1, len(nums)):
                    nums[ix-1] = nums[ix]
                    # print(nums)
            else:
                i += 1
        # print(nums, zero_count)

        while zero_count:
            nums[-zero_count] = 0
            zero_count -= 1

        """
        if nums:

            for i in range(0, len(nums)):
                if i == len(nums) - zero_count:
                    break
                if nums[i] == 0:  # then shift all
                    zero_count += 1
                    for ix in range(i, len(nums)-1):
                        nums[ix] = nums[ix+1]
            print("- "*5)
            print(nums)
            print(zero_count)
            print("- " * 5)

            while zero_count:
                nums[-zero_count] = 0
                zero_count -= 1
        """
        return nums