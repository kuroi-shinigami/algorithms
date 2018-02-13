from unittest import TestCase

from employee_importance import Solution

s = Solution()


class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates


class TestSolution(TestCase):
    """"""

    def test_0(self):
        employees = [Employee(*x) for x in [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]]]
        self.assertEqual(s.getImportance(employees, 1), 11)

    def test_1(self):
        employees = [Employee(*x) for x in [[2, 5, []]]]
        self.assertEqual(s.getImportance(employees, 2), 5)

