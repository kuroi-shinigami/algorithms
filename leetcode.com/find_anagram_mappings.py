#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        res = []
        for x in A:
            res.append(B.index(x))
        return res
