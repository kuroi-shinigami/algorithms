#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Works correctly, but too slow
        # - - - - -
        # if n <= 2:
        #     return 0
        # if n == 3:
        #     return 1
        # res = {2, 3}  # is for 2
        # for x in range(3, n, 2):
        #     # start = max(res) if max(res) != 2 else 3
        #     # print("{}: {} -> {}".format(res, start, x+1))
        #     for i in range(3, x+1, 2):
        #         # print('\t', i)
        #         if not x % i:
        #             break
        #         if i**2 >= x:
        #             res.add(x)
        #             break
        # return len(res)

        # Works correctly, faster, but yet too slow
        # - - - - -
        # def isPrime(n):
        #     if n == 2:
        #         return True
        #     if n == 3:
        #         return True
        #     for x in range(3, n, 2):
        #         if n % x == 0:
        #             return False
        #         if x*x >= n:
        #             return True
        #     return True
        #
        # if n <= 3:
        #     return int(n == 3)
        # res = 1
        # for x in range(3, n, 2):
        #     prime = isPrime(x)
        #     # print(x, prime)
        #     res += int(prime)
        # return res

        # Works correctly, faster, but even now is too slow
        # - - - - -
        # if n <= 2:
        #     return 0
        # # numbers = {x: True for x in [2] + list(range(3, n, 2))}
        # numbers = set(range(3, n, 2))
        # p = 2
        # numbers.add(p)
        # seen = {p}
        # while p*p < n:
        #     print(len(seen), len(numbers))
        #     p = min(numbers - seen)
        #     k = 2
        #     _n = k*p
        #     while _n < n:
        #         numbers.discard(_n)
        #         k += 1
        #         _n = k * p
        #     seen.add(p)
        # return len(numbers)

        if n <= 2:
            return 0
        numbers = [1]*n
        numbers[0] = 0
        numbers[1] = 0
        for p in range(2, int(n**0.5)+1):
            if numbers[p] == 1:
                k = 2
                idx = k * p
                while k * p < n:
                    numbers[idx] = 0
                    k += 1
                    idx = k * p
        return sum(numbers)
