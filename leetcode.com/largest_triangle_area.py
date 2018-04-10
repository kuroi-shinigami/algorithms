#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from itertools import combinations


class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        S = 0
        for triplets in combinations(points, 3):
            sides = [((x[0][0] - x[1][0])**2 + (x[0][1] - x[1][1])**2)**0.5 for x in combinations(triplets, 2)]
            p = sum(sides)/2.0
            # print(p)
            sides = [abs(p - x) for x in sides]
            # print(sides)
            res = 1
            for x in sides:
                res *= x
            res *= p
            if res < 0:
                print(p)
                print(res)
                print(sides)
            res = res ** 0.5
            if res >= S:
                S = res
        return S
