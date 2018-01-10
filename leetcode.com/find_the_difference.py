#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        some_dict = {}
        for x in t:
            if x not in some_dict:
                some_dict[x] = 1
            else:
                some_dict[x] += 1
        for x in s:
            some_dict[x] -= 1  # And del key if it became 0?
        print(some_dict)
        for x in some_dict:
            if some_dict[x]:
                return x