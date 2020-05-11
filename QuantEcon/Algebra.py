from sympy import Symbol
from sympy import solve
from sympy import limit, sin, diff

x, y = Symbol('x'), Symbol('y')
expression = (x + y)**2
print(expression.expand())                  #expand expression

print(solve(x**2 + x + 2))                  #solve expressions

print(limit(1/x, x, 0))                     #calculate limits
print(limit(sin(x)/x, x, 0))

print(diff(sin(x), x))                      #calculate derivatives

