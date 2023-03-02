import timeit

import pandas as pd
import pyspark

from view_error.view_dup import dup_view


def dup(db_filename, co):
    from profiler.SparkClean import sparkclean

    df_path = f'./data/{db_filename}.csv'
    df1 = pd.read_csv(f'./data/{db_filename}.csv')
    df = sparkclean.spark.read.csv(df_path)

    col = [c for c in df.columns]
    tf = sparkclean.DataFrameTransformer(df)
    tf.remove_special_chars(columns=col).clear_accents(columns='*')
    de = sparkclean.DataFrameDeduplicator(df)


    print('\nEnter threshold check for duplicate: Example "0.8" ')
    th = input()
    starttime = timeit.default_timer()
    col, cluster = de.localitySensitiveHashing(col[co], blockSize=3, method="levenshtein", threshold=float(th))
    de.preview(col, cluster)

    pathfile = f'./metadata/duplicates.csv'
    df_dup = pd.read_csv(pathfile, low_memory=False)

    val = []
    for c in df_dup.columns:
        val.append(c)

    print('_________ Duplicates Found--------', len(val), '\n')
    print("\n The time for duplicates detection is :", timeit.default_timer() - starttime, '\n')
    dup_view(df1, len(val), db_filename, val)


