from Equation import Expression
y = input()
y = y.replace('exp', 'math.exp')

x = Expression('x+x')
print(x(y))

import math
print(math.exp(2))