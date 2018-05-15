#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        for row in A:
            _row = []
            for cell in reversed(row):
                if cell == 1:
                    _row.append(0)
                else:
                    _row.append(1)
            res.append(_row)
        return res
