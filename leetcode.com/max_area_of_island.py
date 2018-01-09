#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Not necessary needed (works on platform), but I had to use it locally
        # import sys
        # sys.setrecursionlimit(sys.getrecursionlimit()*2)
        max_size = 0
        seen_ones = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    if (i, j) in seen_ones:
                        pass
                    else:
                        new_dots = self.find_neighbors(i, j, set(), grid)
                        if len(new_dots) > max_size:
                            max_size = len(new_dots)
                        for x in new_dots:
                            seen_ones.add(x)

        return max_size

    def find_neighbors(self, i, j, accum, grid):
        # print(i, j, accum)
        if (i, j) not in accum:
            accum.add((i, j))
            for x, y in [(i, j-1), (i, j+1), (i-1, j), (i+1, j)]:
                if x >= 0 and y >= 0:
                    try:
                        if grid[x][y]:
                            self.find_neighbors(x, y, accum, grid)
                    except IndexError:
                        pass
        return accum
