#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from string import ascii_lowercase


class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morze_letters = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                         "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        alphabet = {x: y for x, y in zip(ascii_lowercase, morze_letters)}
        res = set()
        for word in words:
            s = ''
            for letter in word:
                s += alphabet[letter]
            res.add(s)
        return len(res)
