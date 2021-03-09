import numpy as np
import random

if __name__ != "__main__":
    size = 15
    matrix = np.zeros((size, size), dtype='int64')
    stack_current_move = []
    matrix[1][2] = 1
    matrix[1][14] = 1
    matrix[5][14] = 1
    matrix[5][8] = 1
    matrix[7][2] = 1
    matrix[7][4] = 1
    matrix[11][4] = 1
    matrix[11][8] = 1
