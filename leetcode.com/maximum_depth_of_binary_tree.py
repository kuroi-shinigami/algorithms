#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        res = 1
        res += max(self.maxDepth(root.left), self.maxDepth(root.right))
        return res
