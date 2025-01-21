import copy

def gauss_seidel(a, b, e, m=10000):
    for i in range(len(a)):
        t = a[i][i]
        f = 0
        for j in range(len(a[i])):
            if i ==j:
                continue
            else:
                f+=a[i][j]
        if (t<f):
            print("this is not relevant for jacobi method")
            return None
        
    i = 0
    x = [0] * len(a) 
    while i < m:
        i += 1
        x_old = x.copy() 
        for j in range(len(a)):
            sum_before = 0
            for k in range(j):
                sum_before += a[j][k] * x[k]
            
            sum_after = 0
            for k in range(j + 1, len(a)):
                sum_after += a[j][k] * x_old[k]
            
            x[j] = (b[j] - sum_before - sum_after) / a[j][j]
        
        c = [abs(x_old[k] - x[k]) for k in range(len(a))]
        diff = max(c)
        if diff < e:
            return x
    
    print("The method did not converge within the maximum number of iterations.")
    return x