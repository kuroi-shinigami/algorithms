#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for x in range(1, n+1):
            b = str(x)
            if not x % 3:
                b = "Fizz"
            if not x % 5:
                b = "FizzBuzz" if b == "Fizz" else "Buzz"
            res.append(b)
        return res
