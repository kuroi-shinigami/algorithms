#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        s = ''
        # Dissatisfactory, but fast-accepted solution:
        _romans = {'I': 1,
                   'IV': 4,
                   'V': 5,
                   'IX': 9,
                   'X': 10,
                   'XL': 40,
                   'L': 50,
                   'XC': 90,
                   'C': 100,
                   'CD': 400,
                   'D': 500,
                   'CM': 900,
                   'M': 1000}
        letters = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        for i, x in enumerate(letters):
            count = int(num / _romans[x])
            num = num % _romans[x]
            s += x * count
        return s
