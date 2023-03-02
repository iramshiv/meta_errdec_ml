import csv
import timeit

import pandas as pd


# Find missing values
from view_error.view_null import null_view


def missing_value(df, ccc, db_filename):
    null_constraint(df, ccc, db_filename)

    null_column = df.isnull().sum()
    null_total = df.isna().sum().sum()
    print('column-wise missing values: \n')
    print(null_column, '\n')
    print('Total missing values: \n ', null_total)


# Create null minus dataset
def null_constraint(df, ccc, db_filename):
    starttime = timeit.default_timer()
    #print("The start time is :", starttime)
    df_n = df
    fl = ["./metadata/" + db_filename + "_null.csv", "./metadata/" + db_filename + "_error_log.csv", "./metadata/" + db_filename + "_combo_log.csv"]

    for f in fl:
        with open(f, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(df.columns)

        dff = pd.read_csv(f)
        cov = df[ccc].tolist()
        dff[ccc] = pd.Series(cov)
        dff.to_csv(f, index=False)

        dffb = pd.read_csv(f)
        #df = df.loc[:, ~df.columns.isin([ccc])]

        li = []

        for c in df.columns:
            li.clear()

            for cc in df[c]:
                if pd.isnull(cc):
                    li.append(1)
                else:
                    li.append(0)

            dffb[c] = pd.Series(li)
            dffb.to_csv(f, index=False)

    print("The time for null detection is :", timeit.default_timer() - starttime)

    df_no = df.dropna()

    return df_no
