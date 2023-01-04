'''Task
Given an integer,

, perform the following conditional actions:

    If

is odd, print Weird
If
is even and in the inclusive range of to
, print Not Weird
If
is even and in the inclusive range of to
, print Weird
If
is even and greater than , print Not Weird

Input Format

A single line containing a positive integer,

.

Constraints

Output Format

Print Weird if the number is weird. Otherwise, print Not Weird.'''

# !/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    if n >= 1 and n <= 100:
        if n % 2 is not 0:
            print('Weird')
        else:
            if n >= 2 and n <= 5:
                print('Not Weird')
                pass
            if n >= 6 and n <= 20:
                print('Weird')
                pass
            if n > 20:
                print('Not Weird')
                pass
