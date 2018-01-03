#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        return int(min(len(set(candies)), len(candies)/2))
