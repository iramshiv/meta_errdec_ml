import hashlib
import timeit

import pandas as pd

li = []
val = []
foun = []


def calculate_hash_val(db_filename, cc):
    i = 0
    path = f'./data/{db_filename}.csv'
    df = pd.read_csv(path)

    for c in df[cc]:
        hasher = hashlib.md5()
        hasher.update(c.encode('utf-8'))
        li.append(hasher.hexdigest())

    dfff = set()
    dup = []
    starttime = timeit.default_timer()
    for v in li:
        if v in dfff:
            dup.append(v)
            val.append(i)
            i += 1
        else:
            dfff.add(v)
            i += 1

    for cx in val:
        foun.append(df[cc][cx])

    print('---- The Duplicates found with hash are: ------ \n')
    print(foun)
    xcv = len(foun)
    print(f'--------- The number of duplicates found are ------- {xcv}')
    print("\n The time for duplicates detection is :", timeit.default_timer() - starttime, '\n')
    return foun, xcv


