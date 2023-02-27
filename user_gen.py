from subprocess import Popen, PIPE
import pandas as pd
from Equation import Expression


def user_meta(db_filename):
    data = f'./metadata/length_{db_filename}.csv'
    dd = pd.read_csv(data)

    print(dd.columns)
    print('Enter Column name from above for further generation: ')
    col = input()

    mean = dd.min(col)
    min = dd.min(col)
    max = dd.max(col)

    Meta_name = input("Metadata function name: ")
    expression = input("Enter the formula / Expression: ")
    function = f'{Meta_name} = Expression("{expression}")\n'

    filename = "parse_py.py"
    with open(filename, "a") as f:
        f.write(function)
        f.close()

    generate = input("Enter the arguments:")
    # mean = (f"{generate[0], generate[1]}")
    bas = Popen(['bash'],stdin=PIPE,stdout=PIPE, shell=True)
    bas.stdin.write(b"f'{generate}'")
    out = bas.stdout.read()
    print(out)

    # print(d1)
    # fn = Expression("x+y-n")
    # print(fn)
    # mean = (np.mean(d))
    # print(mean)

    #print(fn(np.array(dd['name']), np.array(dd['addr'])))

