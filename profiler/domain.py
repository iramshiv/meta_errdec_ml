import sys
import timeit

import pandas as pd

from view_error.view_domain import dmv_dom

li = []


def domain_role(db_filename, df):

    for c in df.columns:
        print(c)
    p = str(input('Please enter a column name from above for domain validation'))
    look = input('Please enter the look up directory: (For our work, US phone format "./lookup/phone.txt") ')
    check = [line.strip() for line in open(look)]

    i = 0
    ii = 0
    f = f'./metadata/top_pattern_{db_filename}.csv'
    f1 = pd.read_csv(f)

    starttime = timeit.default_timer()
    li.clear()
    for x in range(len(f1[p])):
        if str(f1[p][x]) not in check:
            i += 1
            li.append(x)


    print('\n Total Domain role integrity constraints: ', i)
    print("\n The time for DMV detection is :", timeit.default_timer() - starttime)
    dmv_dom(df, i, db_filename, li, p)
    #print(li)

