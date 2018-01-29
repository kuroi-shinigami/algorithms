#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        def is_prime(x):
            if x == 2:
                return True
            if not x % 2:
                return False
            i = 3
            while i*i <= x:
                if not x % i:
                    return False
                i += 1
            return True

        res = 0
        d = dict()
        for x in range(L, R+1):
            # key is for number of ones to not recheck the same numers
            key = bin(x).count("1")
            if key > 1:
                if key == 2 or key % 2:
                    if key in d:
                        d[key] += 1
                    else:
                        d[key] = 1
        for k, v in d.items():
            if is_prime(k):
                res += v
        return res

