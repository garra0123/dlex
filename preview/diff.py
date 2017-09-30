from sympy import *

# 定义函数变量x
x = Symbol('x')

# 函数sin（x**2）*x 对x求导
d = diff(sin(x ** 2) * x, x)

print("函数sin(x**2)*x 对x求导: \n%s" % d)
