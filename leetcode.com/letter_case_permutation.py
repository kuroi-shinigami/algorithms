#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = [""]
        for x in S:
            if x.upper() != x.lower():
                if res != [""]:
                    res = res*2
                    for i in range(int(len(res)/2)):
                        res[i] = res[i] + x.lower()
                        res[len(res)-i-1] = res[len(res)-i-1] + x.upper()
                else:
                    res = [x.upper(), x.lower()]
            else:
                if res != [""]:
                    res = [i+x for i in res]
                else:
                    res = [x]
        return res
