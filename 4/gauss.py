import numpy as np

def row_el(a,b,i):
    k  = b[i]/a[i]
    for q in range(len(a)-i):
        b[i+q] =b[i+q] - a[i+q]*k
    return b

def normalize_mat(a):
    for i in range(len(a)):
        for s in range(len(a)-1,i,-1):
            a[s]=row_el(a[i],a[s],i)
    return(len(a))

def join(a, b):
    mat = []
    for i in range(len(a)):
        mat.append(a[i] + [b[i]])
    return mat

def gauss_eleminaton(a, n):
    b = [0] * (n)
    mat = join(a,b)
    normalize_mat(mat)
    n = len(mat)
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = mat[i][-1]  
        for j in range(i + 1, n):
            x[i] -= mat[i][j] * x[j]
        x[i] /= mat[i][i]
    return x    

