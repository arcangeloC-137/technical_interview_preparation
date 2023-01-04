'''To decode the script, Neo needs to read each column and select only the alphanumeric characters and connect them. Neo reads the column from top to bottom and starts reading from the leftmost column.

If there are symbols or spaces between two alphanumeric characters of the decoded script, then Neo replaces them with a single space '' for better readability.

Neo feels that there is no need to use 'if' conditions for decoding.

Alphanumeric characters consist of: [A-Z, a-z, and 0-9].

Input Format

The first line contains space-separated integers
(rows) and (columns) respectively.
The next

lines contain the row elements of the matrix script.

Constraints

Note: A score will be awarded for using 'if' conditions in your code.'''

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []
reg = '\w*'

for j in range(n):
    matrix_item = input()
    row = []
    for i in range(len(matrix_item)):
        row.append(matrix_item[i])
    matrix.append(row)

message = ''
j=0
while(j<m and j<100):
    for i in range(n):
        message = message + matrix[i][j]
    j = j+1

x_clean = " ".join(re.sub("[^a-zA-Z\d\s:]", " ", message).split())

x = re.sub("[^a-zA-Z\d\s:]", " ", message).rstrip()
l = len(x)
y = re.sub("[a-zA-Z\d\s]", " ", message)
last = y[l:len(y)]
before = ''
try:
    first_char = x_clean[0]
    bef_idx = message.index(first_char, 0)
    before = y[0:bef_idx]
except:
    pass

print(before+x_clean+last)