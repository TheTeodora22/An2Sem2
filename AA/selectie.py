import numpy as np
def f(x,a,b,c):
    return a*(x**2) + b*x + c
a,b,c = map(int,input().split())
n = int(input())
xs = [float(xi) for xi in input().split()]
fit = [f(xi,a,b,c) for xi in xs]
suma = sum(fit)
if suma != 0:
    p_sel = [fi / suma for fi in fit]
else:
    p_sel = [0]
q = np.cumsum([0] + p_sel)
for val in q:
    print(f"{val:.6f}".rstrip('0').rstrip('.'))
