#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        # counter = 0
        # if ops:
        #     matrix = [[0 for x in range(m)] for x in range(n)]
        #     for op in ops:
        #         for i in range(op[0]):
        #             for j in range(op[1]):
        #                 matrix[i][j] += 1
        #     # for line in matrix:
        #     #     print(line)
        #     _max = max([max(line) for line in matrix])
        #     for line in matrix:
        #         for cell in line:
        #             if cell == _max:
        #                 counter += 1
        # else:
        #     counter = m*n
        # return counter
        if not ops:
            return m*n
        _m = min([op[0] for op in ops])
        _n = min([op[1] for op in ops])
        return _m*_n
