
def fact(n):
    f = 1;
    for i in range(2, n + 1):
        f *= i;
    return f;


def forward_diff(y):
    for i in range(1,len(y)):
        y[i-1] =  y[i] - y[i - 1];
    y.pop()
    return y[0]

def newton_forward(x, yy, n, x0):
    y = yy.copy()
    sum = y[0];
    h=(x[1] - x[0])
    u = (x0 - x[0]);
    for i in range(1, n):
        sum = sum + (forward_diff(y) * u) / (fact(i)*h**i);
        u *= (x0 - x[i]);
    return sum;

def forward_diffs(y):
    diffs = [y]  
    print()
    print("DIFF TABLE")
    while len(y) > 1:
        y = [y[i] - y[i - 1] for i in range(1, len(y))]
        diffs.append(y)
    for i in range(len(diffs)):
        for j in range(1,len(diffs[i])+1):
            print(f"{i+1}^y{j}: {round(diffs[i][j - 1],2)}", end=" ")
        print()
    return diffs

def missing(y):
    n=len(y)
    d = forward_diffs(y)
    print()
    print("MISSING ITEM")
    return round((d[-1][0]/(n-1)),1)
