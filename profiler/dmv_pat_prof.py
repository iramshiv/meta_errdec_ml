import csv
import timeit

import numpy as np
import pandas as pd

from view_error.view_dmv import dmv_view
from view_error.view_dmv1 import dmv_view1

li = []
dmv_val = []


def dmv_pat(df, index_col, db_filename):
    fdmv = f"./metadata/dmv_pattern_{db_filename}.csv"
    d = pd.read_csv(fdmv)
    fdmv1 = d.loc[:, ~d.columns.isin(index_col)]
    starttime = timeit.default_timer()
    col = [i for i in fdmv1.columns]
    mydict = {}
    for x in col:
        i = 0
        li.clear()
        for c in fdmv1[x]:
            if pd.isnull(c):
                pass
            if list(set(str(c))) == ['S']:
                #print(c)
                li.append(i)
            i += 1
        mydict[x] = np.array(li)

    fd = f"./data/{db_filename}.csv"
    df_fd = pd.read_csv(fd, low_memory=False)
    cv = 0
    for key in mydict:
        for x in range(len(mydict[key])):
            if df_fd[key][mydict[key][x]] not in dmv_val:
                dmv_val.append(df_fd[key][mydict[key][x]])
            cv += 1

    print("\n ---------- DMV from patterns found-----", dmv_val, '\n')
    print("\n -------- Total DMVs found -------", cv, '\n')
    print("\n The time for DMV pattern detection is :", timeit.default_timer() - starttime, '\n')

    return dmv_val
