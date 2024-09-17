from scipy import interpolate
import numpy as np
from matplotlib import pyplot as plt
x = np.linspace(0, 10, 11)
y = np.sin(x)
plt.plot(x, y)
x_new = np.linspace(0, 10, 101)
for kind in ["nearest", "zero", "linear", "quadratic"]:
    f = interpolate.interp1d(x, y, kind=kind)
    y_new = f(x_new)
    plt.plot(x_new, y_new, label=kind)

    
plt.legend()
plt.show()
