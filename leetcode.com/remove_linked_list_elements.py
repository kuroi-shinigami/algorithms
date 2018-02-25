#!/usr/bin/env python
# -*- coding: UTF-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # if head.val == val:
        #     if head.next:
        #         head.val = head.next.val
        #         head.next = head.next.next
        #     else:
        #         return None
        # self.removeElements(head.next, val)
        # return head

        # JUST F*CK TH*S SH*T with their recursion limits. S*ns of the b*tch!

        self = ListNode(0)
        self.next, head = head, self
        while head.next:
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next
        return self.next
