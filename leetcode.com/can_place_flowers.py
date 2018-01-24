#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True
        # Place one flower in the start and in the end
        counter = 0
        while flowerbed[-2:] == [0, 0]:
            n -= 1
            flowerbed = flowerbed[:-2]
        if n <= 0:
            return True
        while flowerbed[:2] == [0, 0]:
            n -= 1
            flowerbed = flowerbed[2:]
        if n <= 0:
            return True
        if len(flowerbed) == 1:
            if flowerbed[0] == 0 and n == 1:
                return True
        # What about [0, 0, 0, 0, 1], 2?
        for x in flowerbed:
            if x:
                counter = 0
            else:
                counter += 1
                if counter == 3:
                    n -= 1
                    if n == 0:  # exit if we know that all plants are already placed
                        return True
                    counter = 1
        return n <= 0
