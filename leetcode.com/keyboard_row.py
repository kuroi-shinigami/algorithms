#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        rows = [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')]
        for word in words:
            for x in rows:
                if set(word.lower()).issubset(x):
                    res.append(word)
                    break
        return res
