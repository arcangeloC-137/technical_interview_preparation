'''Task

You are given a
X integer array matrix with space separated elements ( N = rows and

M = columns).
Your task is to print the transpose and flatten results.

Input Format

The first line contains the space separated values of
and .
The next lines contains the space separated elements of

columns.

Output Format

First, print the transpose array and then print the flatten.

'''
import numpy as np

dim = str(input()).split(" ")

N = int(dim[0])
M = int(dim[1])
inp_arr = []
while(N>0):
    inp_arr.append([int(n) for n in str(input()).split(" ")])
    N-=1

np_array = np.array(inp_arr)
out_transp = np.transpose(np_array)
out_flat = np_array.flatten()
print(out_transp)
print(out_flat)