#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()
        nums.sort()
        if len(nums) > 2:
            if nums[0] == nums[-1]:
                if nums[-1] == 0:
                    return [[0, 0, 0]]
        for i in range(len(nums) - 2):
            s = i + 1
            e = len(nums) - 1
            while s < e:
                _s = nums[i] + nums[s] + nums[e]
                if _s == 0:
                    res.add(tuple([nums[i], nums[s], nums[e]]))
                    if nums[s] == nums[s + 1]:
                        s += 1
                    else:
                        e -= 1
                elif _s > 0:
                    e -= 1
                else:
                    s += 1
        #                                          III-rd attempt. WTF? Just almost the same with accepted option above.
        """        
        res = set()
        nums.sort()
        if len(nums) > 2:
            if nums[0] == nums[-1]:
                if nums[-1] == 0:
                    return [[0, 0, 0]]
        for i in range(len(nums) - 2):
            a = nums[i]
            s = i + 1
            e = len(nums) - 1
            while s < e:
                b = nums[s]
                c = nums[e]
                if a + b + c == 0:
                    res.add(tuple([a, b, c]))
                    if b == nums[s + 1]:
                        s += 1
                    else:
                        e -= 1
                elif a + b + c > 0:
                    e -= 1
                else:
                    s += 1
        # print([list(x) for x in res])
        """

        # print(res)
        #                                                     II-nd, less lazy, less naive, but not fast enough approach
        #                                                                  Requires 'from itertools import combinations'
        """
        res = set()
        less = []
        more = []
        for x in nums:
            less.append(x) if x < 0 else more.append(x)
        counter = 0
        for x in more:
            if x == 0:
                counter += 1
                if counter == 3:
                    res.add(tuple([0, 0, 0]))
                    break
        print('- '*5, len(set(combinations(more, 2))))
        ix = 0
        for _l in set(less):
            for x in set(combinations(more, 2)):
                ix += 1
                # print(ix)
                if abs(_l) == sum(x):
                    _t = tuple(sorted([_l] + list(x)))
                    if _t not in res:
                        res.add(_t)
        print('+ ' * 5, len(set(combinations(less, 2))))
        for _m in set(more):
            for x in set(combinations(less, 2)):
                if -_m == sum(x):
                    _t = tuple(sorted(list(x) + [_m]))
                    if _t not in res:
                        res.add(_t)
        res = list(res)
        # """

        #                                                                        I-st, lazy, naive, brute-force approach
        #                                                                  Requires 'from itertools import combinations'
        """
        res = {tuple(sorted(x)) for x in combinations(nums, 3) if not sum(x)}
        return [list(x) for x in res]
        # """
        return list(res)

