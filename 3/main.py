from lsm import least_square_method
import matplotlib.pyplot as plt

if __name__ == "__main__":
    x = [1, 2, 3, 4, 5]
    y = [1.8, 5.1, 8.9, 14.1, 19.8]
    gaps = [[0],[1]]
    degrees = [1,2,3,4]
    start = 0
    r = []
    count = 0
    plt.scatter(x, y, color='black', label='Data points')

    for degree in degrees:
        for gap in gaps:
            coefficients, ssr = least_square_method(x, y, degree,start,gap)
            print()
            print(f'{count} Coefficients for degree {degree}: {coefficients} / SSR: {ssr} / Gap: {gap}')
            count += 1
            r.append(ssr)
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

                        sum += coefficients[i] * current**p
                        i += 1
                    p += 1
                y_fit.append(sum)

            plt.plot(x_fit, y_fit, label=f'Degree {degree} / Gap {gap}')
    print()
    print(f"Best fit: {r.index(min(r))}")
    plt.grid()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()