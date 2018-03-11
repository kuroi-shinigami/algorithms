#!/usr/bin/env python
# -*- coding: UTF-8 -*-


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        _seen = set()
        h = head
        while h:
            if h not in _seen:
                _seen.add(h)
                h = h.next
            else:
                return True
        return False
