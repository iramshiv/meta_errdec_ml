import csv

import pandas as pd


def csv_writ_id(fname, df, col):
    col_names = [col]
    for c in df.columns:
        col_names.append(c)

    with open(fname, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(col_names)

    id_1 = []

    for i in range(len(df)):
        id_1.append(i)
    dff = pd.read_csv(fname)
    dff[col] = pd.Series(id_1)
    dff.to_csv(fname, index=False)

    for c in df.columns:
        dff[c] = pd.Series(df[c])
        dff.to_csv(fname, index=False)


    return dff
