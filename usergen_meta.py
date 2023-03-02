import numpy as np
import pandas as pd
from Equation import Expression

data = './metadata/length_rest_p.csv'
dd = pd.read_csv(data)

add = Expression("x+y")
x = add(np.array(dd['class']), np.array(dd['name']))

#print(len(x))
#print(x)

y = x[x > 10]
#print(len(y))

ii = 0
lis = []
for i in range(len(x)):
    if x[i] != y[ii]:
        pass
    else:
        ii += 1
        lis.append(i)

#print(len(lis))

