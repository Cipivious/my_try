"""
`interp2d` has been removed in SciPy 1.14.0.

For legacy code, nearly bug-for-bug compatible replacements are
`RectBivariateSpline` on regular grids, and `bisplrep`/`bisplev` for
scattered 2D data.

In new code, for regular grids use `RegularGridInterpolator` instead.
For scattered data, prefer `LinearNDInterpolator` or
`CloughTocher2DInterpolator`.

For more details see
`RectBivariateSpline` on regular grids, and `bisplrep`/`bisplev` for
scattered 2D data.

In new code, for regular grids use `RegularGridInterpolator` instead.
For scattered data, prefer `LinearNDInterpolator` or
`CloughTocher2DInterpolator`.

`RectBivariateSpline` on regular grids, and `bisplrep`/`bisplev` for
scattered 2D data.
"""
from scipy.interpolate import RegularGridInterpolator
import numpy as np
from matplotlib import pyplot as plt
import matplotlib

def func(x, y):
    return (x + y) * np.exp(-5.0 * (x**2 + y**2))

# 原始网格
x = np.linspace(-1, 1, 15)
y = np.linspace(-1, 1, 15)
x_grid, y_grid = np.meshgrid(x, y)

# 函数值
fvals = func(x_grid, y_grid)
print(fvals)
# 创建插值函数
interpolating_function = RegularGridInterpolator((x, y), fvals, method='cubic')

# 新的插值网格
x_new = np.linspace(-1, 1, 100)
y_new = np.linspace(-1, 1, 100)
x_new_grid, y_new_grid = np.meshgrid(x_new, y_new)
fvals_new = interpolating_function((x_new_grid, y_new_grid))

# 可视化
plt.subplot(121)
im1 = plt.imshow(fvals, extent=[-1, 1, -1, 1], cmap=matplotlib.cm.hot, interpolation="nearest", origin="lower")
plt.colorbar(im1)
plt.title("Original Grid")

plt.subplot(122)
im2 = plt.imshow(fvals_new, extent=[-1, 1, -1, 1], cmap=matplotlib.cm.hot, interpolation="nearest", origin="lower")
plt.colorbar(im2)
plt.title("Interpolated Grid")

plt.show()
