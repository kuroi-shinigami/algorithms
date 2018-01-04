#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j]:
                    added_perimeter = 4
                    for ix, iy in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                        if ix >= 0 and iy >= 0:
                            try:
                                added_perimeter -= grid[ix][iy]
                            except IndexError:
                                pass
                    perimeter += added_perimeter
        return perimeter
