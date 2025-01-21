from inverse_matrix import gauss_elimination
import numpy as np
from newton import newton_all_roots

matrix =  np.array([[4, 2, -1],
              [2, 3, 1],
              [-1, 1, 3]])
def det(mat):
    det = np.linalg.det(mat)
    return round(det)

def characteristic_eq(matrix, a):
    matrix_a = [
        [matrix[0][0] - a, matrix[0][1], matrix[0][2]],
        [matrix[1][0], matrix[1][1] - a, matrix[1][2]],
        [matrix[2][0], matrix[2][1], matrix[2][2] - a]
        
    ]
    return round(np.linalg.det(matrix_a))

def f(a):
    return characteristic_eq(matrix,a)

def eigen_values():
    return newton_all_roots(-100,100,0.01,f,100)

def eigenvector(matrix, eigenvalue):
    n = len(matrix)
    matrix_a = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(matrix[i][j] - eigenvalue)
            else:
                row.append(matrix[i][j])
        matrix_a.append(row)

    v = gauss_elimination(matrix_a,n)
    return v

if __name__ == "__main__":
    eigen_vals = eigen_values()
    print("Eigenvalues:")
    print(np.round(eigen_vals))
    print("\nEigenvectors:")
    for eigen_val in eigen_vals:
        eigen_vec = eigenvector(matrix, eigen_val)
        print(np.array(eigen_vec))
