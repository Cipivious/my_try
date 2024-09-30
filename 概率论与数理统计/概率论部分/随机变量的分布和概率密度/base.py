def my_plot(expr, para, start, end, skip=1):
    from matplotlib import pyplot as plt
    X = range(start, end, skip)
    P = [expr.subs(para, x) for x in X]
    plt.plot(X,P)
    plt.show()