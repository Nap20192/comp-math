import copy

def relaxation_method(a, b, o, m=10000):
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
        for i in range(n):  
            sum_before = 0
            for j in range(i):
                sum_before += a[i][j] * x[j]
                
            sum_after = 0
            for j in range(i + 1, n):
                sum_after += a[i][j] * x_old[j]
                
            x[i] = (1 - omega) * x_old[i] + (omega / a[i][i]) * (b[i] - sum_before - sum_after)
        
        c = [abs(x_old[k] - x[k]) for k in range(len(a))]
        diff = max(c)
        if diff < e:
            return x
    
    print("The method did not converge within the maximum number of iterations.")
    return x