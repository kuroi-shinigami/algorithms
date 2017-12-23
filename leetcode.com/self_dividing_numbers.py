#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for x in range(left, right+1):
            if x == 1:
                res.append(1)
            if x > 1:
                _x = set(list([int(k) for k in str(x)]))  #
                if 0 not in _x:
                    for n in _x:  # but there is no need to check '1's!
                        if x % n:
                            break
                    else:
                        res.append(x)
        return res


s = Solution()
print(s.selfDividingNumbers(1, 22))
