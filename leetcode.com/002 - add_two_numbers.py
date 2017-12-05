#!/usr/bin/env python
# -*- coding: UTF-8 -*-


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        d = 0.
        s = d + l1.val + l2.val
        l = ListNode(s % 10)
        d = s // 10
        if l1.next and l2.next:
            l.next = self.addTwoNumbers(l1.next, l2.next)
            if d:
                l.next = self.addTwoNumbers(l.next, ListNode(d))
        elif not (l1.next or l2.next):
            if d:
                l.next = ListNode(d)
        else:
            longer = l2 if l2.next else l1
            if longer.next:
                l.next = longer.next
                if d:
                    l.next = self.addTwoNumbers(l.next, ListNode(d))

        ###
        # Wrong dummy implementations:
        ###
        """                                                                                               II-nd Approach
        d = 0
        s = d + l1.val + l2.val
        l = ListNode(s % 10)
        d = s // 10
        if l1.next and l2.next:
            l.next = self.addTwoNumbers(l1.next, l2.next)
            l.next.val += d
        elif not (l1.next or l2.next):
            if d:
                l.next = ListNode(d)
        else:
            longer = l2 if l2.next else l1
            if longer.next:
                l.next = longer.next
                l.next.val += d
        """
        """                                                                                                I-st Approach
        res = []
        d = 0
        for x, y in zip(l1, l2):
            s = d + x + y
            res.append(s % 10)
            d = s//10
        if len(l1) != len(l2):
            i = l2 if len(l2) > len(l1) else l1
            res.append(i[len(res)] + d)
            return res + i[len(res):]
        return res
        """

        return l
