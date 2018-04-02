#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        res = {}
        for domain in cpdomains:
            count, address = domain.split(" ")
            count = int(count)
            while address:
                if address not in res:
                    res.update({address: count})
                else:
                    res[address] += count
                address = ".".join(address.split(".")[1:])
        return ["{} {}".format(v, k) for k, v in res.items()]
