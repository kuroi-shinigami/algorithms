#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {}
        for x in s:
            if x in count:
                count[x] += 1
            else:
                count[x] = 1
        count = {k: v for k, v in count.items() if v == 1}
        indexes = [s.index(k) for k in count]
        if indexes:
            return min(indexes)
        else:
            return -1