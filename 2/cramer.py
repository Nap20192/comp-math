import numpy as np
import copy

def det(mat):
    det = np.linalg.det(mat)
    return round(det)

def change_col(cof,con,i):
    for a in range(len(cof)):
        cof[a][i] = con[a]
    return cof

def cramer(a, b):
    d = det(a)
    if d == 0:
        return "No unique solution"
    solutions = []
    for i in range(len(b)):
        tm = copy.deepcopy(a)
        tm = change_col(tm,b,i)
        solutions.append(det(tm) / d)
    return solutions
