import csv
import pandas as pd

from profiler.pattern_Learner import learn_patterns


def column_Pattern_Learner(df, df1, ccc, db_filename):

    fname = [f"./metadata/top_pattern_{db_filename}.csv", f"./metadata/data_pattern_{db_filename}.csv",
             f"./metadata/dmv_pattern_{db_filename}.csv", f"./metadata/date_pattern_{db_filename}.csv"]

    for f in fname:
        with open(f, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(df.columns)

        dff = pd.read_csv(f)
        cou = df[ccc].tolist()
        dff[ccc] = pd.Series(cou)
        dff.to_csv(f, index=False)

    df2 = pd.read_csv(fname[0])
    df3 = pd.read_csv(fname[1])
    df4 = pd.read_csv(fname[3])
    df5 = pd.read_csv(fname[2])

    for c in df1.columns:
        # print(c)
        p, p1, p3, p2 = learn_patterns(df[c])
        # print(p)
        # print(p1)
        df2[c] = p
        fi = "./metadata/" + f"top_pattern_{db_filename}.csv"
        df2.to_csv(fi, index=False)
        df3[c] = p1
        fi1 = "./metadata/" + f"data_pattern_{db_filename}.csv"
        df3.to_csv(fi1, index=False)
        df4[c] = p2
        fi2 = "./metadata/" + f"date_pattern_{db_filename}.csv"
        df4.to_csv(fi2, index=False)
        df5[c] = p3
        fi3 = "./metadata/" + f"dmv_pattern_{db_filename}.csv"
        df5.to_csv(fi3, index=False)

