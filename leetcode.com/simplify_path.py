#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = [x for x in path.split('/') if x != '.' and x]
        while '..' in path:
            ix = path.index('..')
            path.pop(ix)
            try:
                if ix > 0:
                    path.pop(ix-1)
            except IndexError:
                pass
        result = '/'.join(path)
        return '/' + result

