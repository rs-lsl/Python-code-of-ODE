# f'(x) = log_10(x+y), y(0)=1
import numpy as np
def true_fun(x):
    return np.exp(x/np.log(10)) - x

def grad(x, y):
    # print(y)
    return np.log10(x+y)

def compute(x0, y0, h):
    # print(y0)
    return y0 + h*grad(x0, y0)

def compute_avg(x0, y0, x1, y1, h):
    return y0 + h*(grad(x0, y0) + grad(x1, y1))/2

y0 = 1
h = 0.2  # interval
N = 5  # number of step
for i in range(0, N):
    y1 = compute(i*0.2, y0, h)
    error = 1
    idx = 0  # the max number of iteration
    print(y1)
    print(f'iter {idx+1}: {y1}')
    while error > 1e-3 and idx< 5:
        y1 = compute_avg(i*h, y0, (i+1)*h, y1, h)
        print(f'iter {idx+2}: {y1}')
        error = np.abs(y1 - true_fun(i*h))
        idx += 1
        print(f'error: {error}')
    y0 = y1
