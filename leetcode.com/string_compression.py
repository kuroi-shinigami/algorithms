#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        # buf = chars[0]
        # counter = 0
        # slices = []
        # for i in range(len(chars)):
        #     if chars[i] == buf:
        #         counter += 1
        #     else:
        #         buf = chars[i]
        #         slices.append(counter)
        #         counter = 1
        # # slices.append(len(chars)-1-sum(slices))
        # print(slices)

        buf = chars[0]
        counter = 0
        slices = []
        for i in range(len(chars)):
            if chars[i] == buf:
                counter += 1
            else:
                buf = chars[i]
                slices.append(counter)
                counter = 1
        slices.append(counter)
        # print(slices)
        start = 0
        for x in slices:
            # print(chars)
            # print(x)
            # print("-"*5)
            if x > 1:
                # pop symbols from start + 1 to start + x
                for i in range(start+1, start + x):
                    # print(chars)
                    chars.pop(start+1)
                # insert counters from start + 1
                for c in reversed(str(x)):
                    chars.insert(start+1, c)
                start = start + len(str(x)) + 1
            else:
                start += x
        # print(chars)
        return len(chars)
