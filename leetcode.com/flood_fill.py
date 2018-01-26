#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if image[sr][sc] != newColor:
            old_color = image[sr][sc]
            image[sr][sc] = newColor
            for x, y in [(sr, sc - 1), (sr, sc + 1), (sr - 1, sc), (sr + 1, sc)]:
                if x >= 0 and y >= 0:
                    try:
                        if old_color == image[x][y]:
                            self.floodFill(image, x, y, newColor)
                    except IndexError:
                        pass
        return image
