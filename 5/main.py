from newtonForward import newton_forward,forward_diffs
import matplotlib.pyplot as plt

if __name__ == '__main__':
    x = [10,20,30,40]
    y = [1.1,2,4.4,7.9]
    x0 = 25
    n = len(x)
    forward_diffs(y)
    print(newton_forward(x,y,n,x0))
