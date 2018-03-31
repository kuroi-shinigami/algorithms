#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        square_root = int(area**0.5)
        if square_root**2 == area:
            return [square_root, int(area**0.5)]
        _delimiter = 1
        for i in range(1, square_root+1):
            if area % i == 0:
                _delimiter = i
        return [int(area/_delimiter), _delimiter]
