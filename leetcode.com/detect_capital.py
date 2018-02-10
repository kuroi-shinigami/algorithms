#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        _word = word.lower()
        if _word == word:
            return True
        if word == word.upper():
            return True
        if _word[0] != word[0]:
            for x, y in zip(word[1:], _word[1:]):
                if x != y:
                    return False
            return True
        return False
