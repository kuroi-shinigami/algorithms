#!/usr/bin/env python
# -*- coding: UTF-8 -*-


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        res = 1
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if not left:
            res += right
            return res
        if not right:
            res += left
            return res
        res += min(left, right)
        return res
