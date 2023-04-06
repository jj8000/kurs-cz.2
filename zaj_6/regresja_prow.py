x = [5, 6, 2, 1, 19, 5]
y = [200, 300, 180, 50, 1100, 580]

import matplotlib.pyplot as plt
from scipy import stats

s, inter, r, p, err = stats.linregress(x, y)

def fun(x):
    return s * x + inter

model = list(map(fun, x))

plt.scatter(x, y)
plt.plot(x, model, color='r')

plt.show()