from unittest import TestCase

from intersection_of_two_linked_lists import Solution

s = Solution()


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def list_to_nodes(some_list):
    if not some_list:
        return
    print(some_list)
    some_list.reverse()
    tail = ListNode(some_list.pop(0))
    tail.next = None
    head = tail  # BUG: head = None causes empty list instead 1-noded
    while some_list:
        head = ListNode(some_list.pop(0))
        head.next = tail
        tail = head
    h = head
    while h:
        print(h.val, end=" ")
        h = h.next
    print()
    return head


class TestSolution(TestCase):
    """"""

    def test_None_0(self):
        l = list_to_nodes([1, 2, 3])
        self.assertEqual(l.val, 1)
        self.assertNotEqual(l.next, None)
        self.assertEqual(l.next.val, 2)
        self.assertNotEqual(l.next.next, None)

    def test_None_1(self):
        l = list_to_nodes([1])
        self.assertEqual(l.val, 1)
        self.assertEqual(l.next, None)

    def test_0(self):
        res = ListNode(6)
        res.next = 7
        self.assertEqual(s.getIntersectionNode(list_to_nodes([1, 3, 5, 6, 7, 8]),
                                               list_to_nodes([2, 4, 6, 7, 8])).val,
                         res.val)
