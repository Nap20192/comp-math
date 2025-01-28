from newtonForward import newton_forward,forward_diffs,missing
import matplotlib.pyplot as plt

if __name__ == '__main__':
    x = [10,20,30,40]
    y = [1.1,2,0,7.9]
    x0 = 25
    n = len(x)
    forward_diffs(y)
    print(missing(y))
