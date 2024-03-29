#!/usr/bin/python3
"""
 calculates the fewest number of operations needed to result
"""


def minOperations(n):
    """returns minimum operations to get n H's"""
    operations = 0
    if n <= 1:
        return 0
    for i in range(2, n + 1):
        while n % i == 0:
            n = n / i
            operations += i
    return operations
