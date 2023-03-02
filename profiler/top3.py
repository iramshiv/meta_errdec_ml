import csv
import timeit

import pandas as pd


def top_values(index_col, db_filename, dmv):
    files = f"./data/{db_filename}.csv"
    df = pd.read_csv(files, low_memory=False)

    fname = f"./metadata/top_values_{db_filename}.csv"
    with open(fname, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(df.columns)

    dff = pd.read_csv(fname, low_memory=False)
    cou = [1, 2, 3, 4, 5]
    dff[index_col[0]] = pd.Series(cou)
    dff.to_csv(fname, index=False)
    df2 = pd.read_csv(fname, low_memory=False)

    df = df.loc[:, ~df.columns.isin(index_col)]
    pattern = []

    for c in df.columns:
        # print(c)
        pattern.clear()
        cou = df[c].value_counts().keys().tolist()
        for q in cou:
            if pd.isnull(q):
                pass
            elif q in dmv:
                pass
            else:
                pattern.append(q)
        # print(pattern)
        df2[c] = pd.Series(pattern[:5])
        df2.to_csv(fname, index=False)
        print(f' Top 5 {c} Values ', pattern[:5])


def top_pat(index_col, db_filename, dmv):
    files = f"./metadata/top_pattern_{db_filename}.csv"

    df = pd.read_csv(files, low_memory=False)
    fname = f"./metadata/top_patterns_{db_filename}.csv"

    with open(fname, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(df.columns)

    dff = pd.read_csv(fname, low_memory=False)
    cou = [1, 2, 3, 4, 5]
    dff[index_col[0]] = pd.Series(cou)
    dff.to_csv(fname, index=False)
    df2 = pd.read_csv(fname, low_memory=False)

    df = df.loc[:, ~df.columns.isin(index_col)]
    pattern = []

    for c in df.columns:
        # print(c)
        pattern.clear()
        cou = df[c].value_counts().keys().tolist()
        for q in cou:
            if pd.isnull(q):
                pass
            elif q in dmv:
                pass
            else:
                pattern.append(q)

        # print(pattern)
        df2[c] = pd.Series(pattern[:5])
        df2.to_csv(fname, index=False)
        print(f' Top 5 {c} Patterns ', pattern[:5])


def top_pat_dat(index_col, db_filename, dmv):
    files = f"./metadata/data_pattern_{db_filename}.csv"
    df = pd.read_csv(files, low_memory=False)

    fname = f"./metadata/top_datapat_{db_filename}.csv"

    with open(fname, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(df.columns)

    dff = pd.read_csv(fname, low_memory=False)
    cou = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    dff[index_col[0]] = pd.Series(cou)
    dff.to_csv(fname, index=False)
    df2 = pd.read_csv(fname, low_memory=False)

    df = df.loc[:, ~df.columns.isin(index_col)]
    pattern = []

    for c in df.columns:
        # print(c)
        pattern.clear()
        cou = df[c].value_counts().keys().tolist()
        for q in cou:
            if pd.isnull(q):
                pass
            elif q in dmv:
                pass
            else:
                pattern.append(q)

        # print(pattern)
        df2[c] = pd.Series(pattern[:15])
        df2.to_csv(fname, index=False)


def top_profiler(db_filename, index_col):
    f = f'./metadata/top_values_{db_filename}.csv'
    f1 = f'./metadata/top_patterns_{db_filename}.csv'
    df = pd.read_csv(f)
    df2 = pd.read_csv(f1)
    df = df.loc[:, ~df.columns.isin(index_col)]
    df2 = df2.loc[:, ~df2.columns.isin(index_col)]
    patterns = []
    err = []
    starttime = timeit.default_timer()
    for ccc in df.columns:
        lis = df2[ccc].tolist()
        for v in df[ccc]:

            pi = ''
            v = str(v)
            for c in v:

                if c in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                         't',
                         'u', 'v', 'w', 'x', 'y', 'z']:
                    p = 'l'
                    pi = pi + p
                elif c in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                           'S',
                           'T',
                           'U', 'V', 'W', 'X', 'Y', 'Z']:
                    p = 'U'
                    pi = pi + p
                elif c in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                    p = 'd'
                    pi = pi + p
                elif c == ' ':
                    p = ' '
                    pi = pi + p
                else:
                    pi = pi + c
            if pi in lis:
                pass
            else:
                print(f"The {v} in {ccc} is not in top patterns, might be potential error.")

    print("\nThe time for top 10 value vs pattern check is : ", timeit.default_timer() - starttime, '\n')