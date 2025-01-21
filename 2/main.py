import numpy as np
from cramer import cramer
from gauss import gauss
from gauss_jordan import gauss_jordan

if __name__ == "__main__":
    a = [[10,-7,3,5],
         [-6,8,-1,-4],
         [3,1,4,11],
         [5,-9,-2,4]]  
    b = [6,5,2,7]  
    print("cramer: ",cramer(a, b))
    print("gauss:",gauss(a,b))
    print("gauss_jordan:",gauss_jordan(a,b))