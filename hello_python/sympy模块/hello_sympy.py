import sympy

sympy.init_printing()

# 定义符号
t, omiga0, gamma = sympy.symbols("t omega_0 gamma", positive=True)
x = sympy.Function("x")
sympy.pprint(t)
sympy.pprint(omiga0)
sympy.pprint(gamma)
# 定义微分方程
ode = x(t).diff(t, 2) + 2 * gamma * omiga0 * x(t).diff(t) + omiga0**2 * x(t)

# 求解微分方程
ode_sol = sympy.dsolve(ode)
sympy.pprint(ode_sol)

# 定义初始条件
init_conditions = {
    x(0): 1,
    x(t).diff(t).subs(t, 0): 0
}

# 应用初始条件
x_t_sol = sympy.dsolve(ode, ics=init_conditions)

# 打印结果
sympy.pprint(x_t_sol)
