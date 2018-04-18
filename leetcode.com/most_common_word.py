#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        punctuation = "!?',;."
        for x in punctuation:
            paragraph = paragraph.replace(x, "")
        paragraph = [x.lower() for x in paragraph.split(' ')]
        counter = dict()
        banned = set(banned)
        max_counter = 0
        for x in paragraph:
            if x not in banned:
                if x not in counter:
                    counter[x] = 1
                else:
                    counter[x] += 1
                if counter[x] > max_counter:
                    max_counter = counter[x]
        for k, v in counter.items():
            if v == max_counter:
                return k
