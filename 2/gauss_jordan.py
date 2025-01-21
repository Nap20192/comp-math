import numpy as np

def row_el(a,b,i):
    k  = b[i]/a[i]
    for q in range(len(a)-i):
        b[i+q] = b[i+q] - a[i+q]*k
    return b

def normalize_mat(a):
    for i in range(len(a)):
        for s in range(len(a)-1,i,-1):
            a[s]=row_el(a[i],a[s],i)
    return(len(a))

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

def el(a):
    n = len(a)
    for i in range(n - 1, -1, -1): 
        for j in range(i - 1, -1, -1):
            f = a[j][i] / a[i][i]
            for k in range(len(a[0])):  
                a[j][k] -= f * a[i][k]
    for i in a:
        print(i)
    return a

def gauss_jordan(a):
    n = len(a)
    b = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    mat = join(a,b)
    normalize_mat(mat)
    mat = to_i(mat)    
    s = el(mat)
    Inv = [row[len(a):] for row in mat]
    return Inv


