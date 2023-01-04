'''You are given a space separated list of nine integers. Your task is to convert this list into a X NumPy array.'''
import numpy as np

int_list = [int(n) for n in str(input()).split(" ")]
print(np.reshape(int_list, (3,3)))
