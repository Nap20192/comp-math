from lsm import least_square_method
import matplotlib.pyplot as plt

if __name__ == "__main__":
    x = [1, 2, 3, 4, 5, 6, 7, 8]
    y = [5.4, 6.3, 8.2, 10.3, 12.6, 14.9, 17.3, 19.5]
    gap = [0]
    degrees = [1]
    start = -1

    plt.scatter(x, y, color='black', label='Data points')

    for degree in degrees:
        coefficients = least_square_method(x, y, degree,start,gap)
        x_fit = []
        current = min(x)
        step=0.3
        while current < max(x):
            x_fit.append(current)
            current += step
        y_fit = []
        current = min(x)
        while current < max(x):
            current += 0.3
            sum = 0
            i = 0
            p = start
            while i <=degree-start-len(gap):
                if p not in gap:
                    print("p",p)
                    print("i",i)
                    sum += coefficients[i] * current**p
                    i += 1
                p += 1
            y_fit.append(sum)

        plt.plot(x_fit, y_fit, label=f'Degree {degree}')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()