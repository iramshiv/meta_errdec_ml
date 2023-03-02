import ast
import os
import statistics
import pandas as pd
import numpy as np
import scipy
from Equation import Expression
from scipy.stats._mstats_basic import winsorize


def winsorized_mean(x, ql, qr):
    return np.mean(winsorize(x, limits=(ql, qr)))


def winsorized_std(x, ql, qr):
    return np.std(winsorize(x, limits=(ql, qr)))


def gen_meta(db_filename):
    data = f'./metadata/length_{db_filename}.csv'
    dd = pd.read_csv(data)

    Meta_name = input("Metadata function name: ")

    for cc in dd.columns:
        print(cc)

    generate = input("Enter the column name to profile:")
    print('Mean ', dd[generate].dropna().mean(), '\nSD ', statistics.stdev(dd[generate].dropna()),
          '\nQuantile ', dd[generate].quantile([0.25, 0.75]), '\nMedian ', dd[generate].dropna().median(),
          '\nMAD ', (dd[generate].dropna() - dd[generate].mean()).abs().mean(), '\ntrimmed mean ',
          scipy.stats.mstats.tmean(dd[generate].dropna())
          , '\ntrimmed SD ', scipy.stats.mstats.trimmed_std(dd[generate].dropna()),
          '\nWinsorized mean', winsorized_mean(dd[generate].dropna(), 0.1, 0.1),
          '\nWinsorized SD', winsorized_std(dd[generate].dropna(), 0.1, 0.1))
    # print(np.array(dd[cc]))

    expression = input("Enter the expression for metetadata generation + heuristics: ")
    expression = expression.replace("exp", "math.exp")
    function = f'{Meta_name} = Expression("{expression}")\n'
    c = f"{Meta_name}_1 = {Meta_name}(np.array(dd['{generate}']))"
    print(c)

    filename = "user_gen_meta_prof.py"
    with open(filename, "a") as f:
        f.write("import numpy as np\nimport pandas as pd\nfrom Equation import Expression\nimport math\n")
        f.write("from view_error.view_meta import meta_view\n")
        f.write(f"original = './data/{db_filename}.csv'\n")
        f.write(f"d1 = pd.read_csv(original, usecols=['{generate}'])\n")
        f.write(f"data = './metadata/length_{db_filename}.csv'\n")
        f.write(f"dd = pd.read_csv(data)\n")
        f.write(f"{function}\n")
        f.write(f"{c}\n")
        f.write(f'print({Meta_name}_1)\n')
        f.write(f'i = 0\n')
        f.write(f'li =[]\n')
        f.write(f"for z in range(len(dd['{generate}'])):\n")
        f.write(f'    if {Meta_name}_1[z] == True:\n')
        f.write(f'        i += 1\n')
        f.write(f'        li.append(z)\n')
        f.write(f"meta_view(d1, i, 'length_{db_filename}', li, '{generate}')\n")
        f.close()

    c = os.system(f"C:/cygwin64/bin/bash --login -c 'cd C:/Users/Sethu/PycharmProjects/errorDetection_Metadata/;"
                  f"python user_gen_meta_prof.py;'")
    os.close(c)

    f = open(filename, 'w').close()


def user_meta(db_filename):
    data = f'./metadata/length_{db_filename}.csv'
    dd = pd.read_csv(data)

    Meta_name = input("Metadata Heuristic name: ")

    if Meta_name == 'val_len_outlier':
        for cc in dd.columns:
            print(cc)

        generate = input("Enter the column name to profile:")
        print('quantile', dd[generate].quantile([0.25, 0.75]))
        print(np.array(dd[cc]))

        expression = input("Enter the formula for lower boundary: ")
        function = f'{Meta_name} = Expression("{expression}")\n'
        c = f"xx = {Meta_name}(np.array(dd['{generate}']))"
        print(c)

        expression1 = input("Enter the formula for upper boundary: ")
        function1 = f'{Meta_name} = Expression("{expression1}")\n'
        c1 = f"yy = {Meta_name}(np.array(dd['{generate}']))"
        print(c1)

        filename = "user_gen_meta_prof.py"
        with open(filename, "a") as f:
            f.write("import numpy as np\nimport pandas as pd\nfrom Equation import Expression\n")
            f.write("from view_error.view_meta import meta_view\n")
            f.write(f"data = './metadata/length_{db_filename}.csv'\n")
            f.write(f"dd = pd.read_csv(data)\n")
            f.write(f"original = './data/{db_filename}.csv'\n")
            f.write(f"d1 = pd.read_csv(original, usecols=['{generate}'])\n")
            f.write(f"{function}\n")
            f.write(f"{c}\n")
            f.write(f'print(xx)\n')
            f.write(f"{function1}\n")
            f.write(f"{c1}\n")
            f.write(f'print(yy)\n')
            f.write(f'zz = xx | yy\n')
            f.write(f'i = 0\n')
            f.write(f'li =[]\n')
            f.write(f"for z in range(len(d1['{generate}'])):\n")
            f.write(f'    if zz[z] == True:\n')
            f.write(f'        i += 1\n')
            f.write(f'        li.append(z)\n')
            f.write(f"meta_view(d1, i, 'length_{db_filename}', li, '{generate}')\n")
            f.close()

        c = os.system(f"C:/cygwin64/bin/bash --login -c 'cd C:/Users/Sethu/PycharmProjects/errorDetection_Metadata/;"
                      f"python user_gen_meta_prof.py;'")
        os.close(c)

        f = open(filename, 'w').close()
        # f.truncate(0)

        # print(d1)
        # fn = Expression("x+y-n")
        # print(fn)
        # mean = (np.mean(d))
        # print(mean)

        # print(fn(np.array(dd['name']), np.array(dd['addr'])))
