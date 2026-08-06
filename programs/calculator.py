#!/usr/bin/env python3
"""Minimal command-line calculator: add, sub, mul, div."""

import sys

def calc(a, b, op):
    if op == 'add':
        return a + b
    if op == 'sub':
        return a - b
    if op == 'mul':
        return a * b
    if op == 'div':
        return a / b
    raise ValueError('unknown op')

def main():
    if len(sys.argv) != 4:
        print('Usage: calculator.py <add|sub|mul|div> <num1> <num2>')
        return
    op = sys.argv[1]
    a = float(sys.argv[2])
    b = float(sys.argv[3])
    try:
        print(calc(a, b, op))
    except Exception as e:
        print('Error:', e)

if __name__ == '__main__':
    main()
