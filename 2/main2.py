from jacobi import jacobi
from gauss_jordan import gauss_jordan
if __name__ == "__main__":

    a = [[2,1,1],
         [1,3,-1],
         [-1,1,2]]  
    b = [[1,0,0],
         [0,1,0],
         [0,0,1]]  
    print("gauss_seidel: ",gauss_jordan(a))