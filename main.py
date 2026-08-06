#!/usr/bin/env python3
"""Compute factorial of a non-negative integer."""

import sys

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def main():
    if len(sys.argv) < 2:
        print('Usage: factorial.py <non-negative-integer>')
        return
    n = int(sys.argv[1])
    if n < 0:
        print('Must be non-negative')
        return
    print(factorial(n))

if __name__ == '__main__':
    main()
