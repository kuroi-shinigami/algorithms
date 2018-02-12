#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t is None:
            return ''
        s = str(t.val)
        if (t.right is None) and (t.left is None):
            return s
        if t.right is None:
            s += '({})'.format(self.tree2str(t.left))
            return s
        s += '({})({})'.format(self.tree2str(t.left), self.tree2str(t.right))
        return s
