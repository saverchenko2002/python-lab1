import numpy as np
import random

if __name__ != "__main__":
    size = 15
    matrix = np.zeros((size, size), dtype='int64')
    matrix[1][2] = 1
    matrix[12][2] = 1
    matrix[12][4] = 1
    matrix[14][4] = 1
    matrix[14][9] = 1
    matrix[1][9] = 1
