#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vovels = {'a', 'e', 'i', 'o', 'u'}
        res = []
        for i, word in enumerate([x for x in S.split(" ") if x.strip()]):
            if word[0].lower() in vovels:
                _w = word
            else:
                _w = word[1:] + word[0]
            res.append(_w + 'ma' + 'a'*(i+1))
        return " ".join(res)
