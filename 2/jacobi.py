import copy

def jacobi(a,b,e,m=10000):
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
    
    i=0
    x = [0] * len(a)

    while i<m:
        i+=1
        x_old = x.copy()
        for j in range(len(a)):
            sum = 0
            for k in range(len(a[j])):
                    if k != j:
                        sum += a[j][k] * x[k]
            x[j] = (b[j]-sum)/a[j][j]
        c = []  
        for k in range(len(a)):
            d = abs(x_old[k] - x[k])  
            c.append(d)
        diff = max(c)
        if diff<e:
            return x