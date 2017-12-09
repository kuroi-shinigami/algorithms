#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(set(s)) == len(s):
            return len(s)
        else:
            # Brute force!11
            s = list(s)
            longest = 0
            substr = set()  # Previosly wat time out error with list. Hash tables are magic!
            i = 0
            # we do not need to search the whole str if longest is greater than left str
            # can't explain (intuition) but it worked!
            while len(s) - i > longest:
                for letter in s[i:]:
                    if letter not in substr:
                        substr.add(letter)
                    else:
                        if len(substr) > longest:
                            longest = len(substr)
                        substr = set()
                        i += 1
                        break

            ###
            # Wrong dummy implementations:
            ###
            """                                                                II-nd approach: wrong assume about slices  
            if len(set(s)) == len(s):
                return len(s)
            else:
                lenght = []
                for x in s:
                    for k in s.split(x):
                        lenght.append(len(k))
                return max(lenght)
            """

            """                                I-st approach: wrong calculation of longest substring with unique letters
            last = 0
            current = 0
            substring_symbols = []  # ToDo: use set
            # I may just handle two listst instead of counters but it should be more expensive in space
            for _x in s:
                if _x not in substring_symbols:
                    substring_symbols.append(_x)
                    current += 1
                    if current > last:
                        last = current
                else:
                    ix = substring_symbols.index(_x)
                    head = substring_symbols[ix:]
                    tail = substring_symbols[:ix]
                    substring_symbols = head if len(head) > len(tail) else tail
                    # substring_symbols.append(_x)
                    current = len(substring_symbols)
            return max(current, last)
            """

            return longest
