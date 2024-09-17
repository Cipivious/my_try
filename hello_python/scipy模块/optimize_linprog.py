"""
max z = 2*x1 + 3*x2 - 5*x3
st:
    x1 + x2 + x3 = 7
    2*x1 - 5*x2 + x3 >= 10
    x1 + 3*x2 +x3 <= 12
    x1, x2, x3 >= 0
"""

from scipy import optimize
import numpy as np

# 设置打印选项
np.set_printoptions(precision=4, suppress=True)
# 定义目标函数的系数 (因为要最大化，目标函数系数取负)
c = np.array([2, 3, -5])

# 定义不等式约束 Ax <= b
A = np.array([[-2, 5, -1], [1, 3, 1]])
b = np.array([-10, 12])

# 定义等式约束 Aeq * x = beq
Aeq = np.array([[1, 1, 1]])
beq = np.array([7])

# 调用线性规划求解函数
res = optimize.linprog(-c, A_ub=A, b_ub=b, A_eq=Aeq, b_eq=beq, bounds=(0, None))

# 输出结果
print(res)

max_num = res.fun
x_list = res.x

true_result = np.dot(-c, x_list)
print(-true_result)
print(-max_num)