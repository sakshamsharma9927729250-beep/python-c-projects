#!/usr/bin/env python3
"""Check whether input string is a palindrome."""

import sys

def is_palindrome(s):
    s2 = ''.join(ch.lower() for ch in s if ch.isalnum())
    return s2 == s2[::-1]

def main():
    if len(sys.argv) < 2:
        print('Usage: palindrome.py <string>')
        return
    s = ' '.join(sys.argv[1:])
    print('Palindrome' if is_palindrome(s) else 'Not palindrome')

if __name__ == '__main__':
    main()
