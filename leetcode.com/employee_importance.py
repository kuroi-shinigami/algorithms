#!/usr/bin/env python
# -*- coding: UTF-8 -*-


"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""


class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        # print("I'm {} and my importance is {} and my subordinates are: {}"
        #       .format(id, employees[id-1].importance, employees[id-1].__dict__))
        if type(employees) is list:
            employees = {x.id: x for x in employees}
        res = employees[id].importance
        for x in employees[id].subordinates:
            res += self.getImportance(employees, x)
        return res
