#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        s = set(list1) & set(list2)
        res = {}
        for l in [list1, list2]:
            for i, x in enumerate(l):
                if x in s:
                    if x in res:
                        res[x] += i
                    else:
                        res[x] = i
        _m_ix = min(res.values())
        return [x for x in res if res[x] == _m_ix]
