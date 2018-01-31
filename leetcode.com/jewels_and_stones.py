#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        res = 0
        for s in S:
            if s in J:
                res += 1
        return res
