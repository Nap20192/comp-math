import numpy as np

def row_el(a,b,i):
    k  = b[i]/a[i]
    for q in range(len(a)-i):
        b[i+q] = b[i+q] - a[i+q]*k
    return b

def diag(a):
    for i in range(len(a)):
        for s in range(len(a)-1,i,-1):
            a[s]=row_el(a[i],a[s],i)

def join(a, b):
    mat = []
    for i in range(len(a)):
        mat.append(a[i] + b[i])
    return mat

def to_i(a):
    for i in range(len(a)):
        k=a[i][i]
        a[i][i]/=k
        for j in range(i+1,len(a[i])):
            a[i][j]/=k
    return a

def to_diag(a):
    n = len(a)
    for i in range(n - 1, -1, -1): 
        for j in range(i - 1, -1, -1):
            f = a[j][i] / a[i][i]
            for k in range(len(a[0])):  
                a[j][k] -= f * a[i][k]
    for i in a:
        print(i)
    return a

def inverse(a):
    n = len(a)
    b = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    mat = join(a,b)
    diag(mat)
    mat = to_i(mat)    
    s = to_diag(mat)
    Inv = [row[len(a):] for row in mat]
    return Inv


if __name__ == "__main__":
    M = [[1, 1 / 2],
        [1 / 2, 1 / 3]]

    for row in inverse(M):
        print(row)



















def gauss_elimination(matrix_a, n):
    vector = [1] + [0] * (n - 1)
    for i in range(n):
        if matrix_a[i][i] != 0:
            factor = matrix_a[i][i]
            for j in range(n):
                matrix_a[i][j] /= factor
        for k in range(i + 1, n):
            factor = matrix_a[k][i]
            for j in range(n):
                matrix_a[k][j] -= factor * matrix_a[i][j]
    vector = [0] * n  
    for i in range(n - 1, -1, -1):
        if any(matrix_a[i]): 
            vector[i] = 1
            for j in range(i + 1, n):
                vector[i] -= matrix_a[i][j] * vector[j]
    return vector


















